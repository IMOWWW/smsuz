from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sms
from .serializers import SMSCallbackSerializer
from .utils import generate_transmit_access_token

from django.conf import settings


class SMSCallbackView(APIView):
    serializer_class = SMSCallbackSerializer

    def post(self, request, *args, **kwargs):
        print(request.headers)
        print(request.data)
        # Validate the request data
        serializer = SMSCallbackSerializer(data=request.data)
        
        if serializer.is_valid():
            # Extract validated data
            transactionid = serializer.validated_data['transactionid']
            smsid = serializer.validated_data['smsid']
            status_value = serializer.validated_data['status']
            description = serializer.validated_data['description']
            statusdate = serializer.validated_data['statusdate']
            partinfo = serializer.validated_data['partinfo']
            
            # Generate the expected access token using the validated status date
            access_token = request.headers.get('X-Access-Token')
            expected_token = generate_transmit_access_token(settings.SAYQAL_USERNAME, settings.SAYQAL_SECRETKEY, statusdate)

            # Validate the access token
            if access_token != expected_token:
                return Response("Bad access token", status=status.HTTP_403_FORBIDDEN)

            # Add your processing logic here (e.g., update the status in your database)
            sms = Sms.objects.get(id=int(smsid))
            sms.transactionid = transactionid
            sms.status = status_value
            sms.partinfo = partinfo
            sms.save()
            return Response("ok", status=status.HTTP_200_OK)
        
        # If validation fails, return a 400 error with the serializer errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
