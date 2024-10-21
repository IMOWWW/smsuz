from rest_framework import serializers

class SMSCallbackSerializer(serializers.Serializer):
    transactionid = serializers.IntegerField(required=True)
    smsid = serializers.CharField(required=True)
    status = serializers.ChoiceField(choices=[0, 1, 2], required=True)
    description = serializers.ChoiceField(choices=["DELIVERED", "UNDELIVERED", "EXPIRED"], required=True)
    statusdate = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", input_formats=["%Y-%m-%d %H:%M:%S"], required=True)
    partinfo = serializers.CharField(required=True)

