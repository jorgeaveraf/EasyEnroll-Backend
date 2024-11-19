# easyenroll/utils/firebase_middleware.py
from django.utils.deprecation import MiddlewareMixin
from graphql import GraphQLError
from easyenroll.utils.firebase_auth import verify_firebase_token
from easyenroll.utils.firebase_user import FirebaseUser

class FirebaseAuthMiddleware(MiddlewareMixin):
    def resolve(self, next, root, info, **kwargs):
        # 1. Start token validation
        print("Middleware de Firebase: Iniciando la validación del token...")

        # 2. Obtain the authorization header
        request = info.context
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        print(f"Encabezado de autorización: {auth_header}")  # Display the authorization header

        # 3. Check if the authorization header is present
        if auth_header:
            token = auth_header.split(' ').pop()  # Extract the token without "Bearer"
            print(f"Token recibido: {token}")  # Display the extracted token
            
            # 4. Verify the token using the `verify_firebase_token` function
            decoded_token = verify_firebase_token(token)
            if not decoded_token:
                print("Middleware de Firebase: Token no válido o expirado")
                raise GraphQLError("Invalid or expired Firebase token")

            # 5. If the token is valid, attach user info using FirebaseUser
            info.context.user = FirebaseUser(decoded_token)
            print("Middleware de Firebase: Token válido, usuario autenticado")
        else:
            print("Middleware de Firebase: Falta el encabezado de autorización")
            raise GraphQLError("Authorization header missing")

        # 6. Continue to the next resolver if everything is valid
        print("Middleware de Firebase: Continuando con el resolver...")
        return next(root, info, **kwargs)
