from django.utils.deprecation import MiddlewareMixin
from firebase_admin import auth
from graphql import GraphQLError
from easyenroll.utils.firebase_auth import verify_firebase_token

class FirebaseAuthMiddleware(MiddlewareMixin):
    def resolve(self, next, root, info, **kwargs):
        # Obtén el encabezado Authorization de la solicitud
        request = info.context
        auth_header = request.META.get('HTTP_AUTHORIZATION')

        if auth_header:
            token = auth_header.split(' ').pop()  # Obtiene el token (sin el prefijo "Bearer")
            decoded_token = verify_firebase_token(token)

            if not decoded_token:
                raise GraphQLError("Invalid or expired Firebase token")

            # Si es válido, adjunta la información del usuario a `info.context`
            info.context.user = decoded_token  # Decoded token contiene la info del usuario en Firebase
        else:
            raise GraphQLError("Authorization header missing")

        # Continua con el siguiente resolver si todo es válido
        return next(root, info, **kwargs)
