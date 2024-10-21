
# smsuz

A Python library for sending SMS via the [Sayqal.uz](https://sayqal.uz) SMS gateway. This library allows you to send SMS messages from your Django application easily.

## Installation

Install the package via `pip`:

```bash
pip install smsuz
```

## Setup

1. Add the `sms` application to your Django project's installed apps. Open your `settings.py` file and update as follows:

   ```python
   INSTALLED_APPS = [
       ...
       'sms',
   ]
   ```

2. Add the `SAYQAL_USERNAME` and `SAYQAL_SECRETKEY` constants to your project settings, which you can obtain after registering on [Sayqal.uz](https://sayqal.uz):

   ```python
   # settings.py

   SAYQAL_USERNAME = 'your_username_here'
   SAYQAL_SECRETKEY = 'your_secretkey_here'
   ```

3. Run the database migrations to apply any necessary changes:

   ```bash
   python manage.py migrate
   ```

## Usage

Import the `sendSms` function and use it to send SMS messages:

```python
from sms.utils import sendSms

# Example of sending an SMS
sendSms('+998971234567', 'Your SMS message text')
```

### Example

```python
from sms.utils import sendSms

# Send an SMS to the specified phone number
phone_number = '+998971234567'
message = 'Your confirmation code: 123456'
sendSms(phone_number, message)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

by AbexLab
