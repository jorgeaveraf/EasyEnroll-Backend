from firebase_admin import auth

def verify_firebase_token(token):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token  # Devuelve el token decodificado si es válido
    except Exception as e:
        print(f"Error verifying Firebase token: {e}")
        return None  # Token inválido o error
