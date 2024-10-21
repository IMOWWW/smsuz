from django.urls import path
from .views import SMSCallbackView
urlpatterns = [
    path('callback/', SMSCallbackView.as_view(), name='sms-callback-view')
]