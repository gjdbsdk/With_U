
from django.urls import path
from .views import RegisterView, LoginView, LogoutView, CitizenContentUploadAPI, CheckLoginAPI

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("citizen/upload/", CitizenContentUploadAPI.as_view()),
    path("check-login/", CheckLoginAPI.as_view(), name="check-login"),
]

