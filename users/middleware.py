import jwt
from django.http import JsonResponse
from django.conf import settings
from .models import User


PUBLIC_ROUTES = [
    "/register/",
    "/login/",
]

class JWTAuthenticationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.path.startswith("/admin"):
            return self.get_response(request)

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            request.user = None
            return self.get_response(request)

        try:
            token = auth_header.split(" ")[1]

            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

            user_id = payload.get("user_id")

            user = User.objects.filter(id=user_id).first()

            request.user = user

        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token expired"}, status=401)

        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Invalid token"}, status=401)

        return self.get_response(request)

