from firebase_admin import auth
from django.contrib.auth.models import AnonymousUser

def verify_firebase_token(token):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token  # Devuelve el token decodificado si es válido
    except Exception as e:
        return AnonymousUser()  # Return an AnonymousUser instead of None
