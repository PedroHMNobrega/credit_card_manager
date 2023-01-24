from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()


def create_jwt(user: User):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)
