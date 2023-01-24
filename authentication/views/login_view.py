from rest_framework import views, status
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from authentication.utils import create_jwt


class LoginView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(username=email, password=password)
        if user is not None:
            token = create_jwt(user)
            return Response({'accessToken': token})
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
