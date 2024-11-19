# easyenroll/utils/firebase_user.py

class FirebaseUser:
    def __init__(self, decoded_token):
        self._decoded_token = decoded_token

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    @property
    def uid(self):
        return self._decoded_token.get("uid")

    @property
    def email(self):
        return self._decoded_token.get("email")

    # You can add other properties as needed, based on your Firebase token data
