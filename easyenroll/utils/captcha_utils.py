# easyenroll/utils/captcha_utils.py
import requests
from django.conf import settings

def verify_recaptcha(token):
    """
    Verifica el token de Google reCAPTCHA.
    """
    url = "https://www.google.com/recaptcha/api/siteverify"
    data = {
        'secret': settings.RECAPTCHA_SECRET_KEY,
        'response': token
    }
    response = requests.post(url, data=data)
    result = response.json()

    return result.get('success', False)
