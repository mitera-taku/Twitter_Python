from rest_framework.authentication import BaseAuthentication # type: ignore
from rest_framework.exceptions import AuthenticationFailed # type: ignore
from rest_framework.authtoken.models import Token # type: ignore

class CookieTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token_key = request.COOKIES.get('auth_token')
        if not token_key:
            return None

        try:
            token = Token.objects.get(key=token_key)
        except Token.DoesNotExist:
            raise AuthenticationFailed("Invalid Token")

        return (token.user, token)
