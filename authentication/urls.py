from django.urls import path
from authentication.views import LoginView, UserView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('user/', UserView.as_view(), name="user")
]
