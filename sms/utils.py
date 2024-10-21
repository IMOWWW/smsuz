import hashlib
import time
import json
import requests
from django.conf import settings
from .models import Sms


def generate_transmit_access_token(user_name, secret_key, status_date):
    access_string = f"TransmitSMSStatus {user_name} {secret_key} {status_date}"
    return hashlib.md5(access_string.encode()).hexdigest()


def sendSms(phone_number, text):
    url = "https://routee.sayqal.uz/sms/TransmitSMS"
    utime = int(time.time())
    token = hashlib.md5(" ".join(["TransmitSMS", settings.SAYQAL_USERNAME, settings.SAYQAL_SECRETKEY, str(utime)]).encode('utf-8')).hexdigest()
    cropped_phone_number = ''.join(phone_number).replace('+', '')

    sms_model = Sms.objects.create(phone_number=phone_number, text=text)

    
    sms = {
        "utime": utime,
            "username": settings.SAYQAL_USERNAME,
            "service": {
                "service": 2
            },
        "message": {
            "smsid": sms_model.id,
            "phone": cropped_phone_number,
            "text": text
        }
    }
    smsJson = json.dumps(sms)

    try:
        response = requests.post(url, json=sms, headers={"Content-Type": "application/json", "X-Access-Token": token}, )
        print(response.status_code)
        if response.status_code == 200:
            # success
            print(response.json())
        elif response.status_code == 400:
                # param(s) invalid
            print(response.json())
        else:
            # 403 - token invalid
            print("token invalid")
    except requests.ConnectionError:
        print("failed to connect")
