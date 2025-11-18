
from django.urls import path

from .views import LoginView, LogoutView, RegisterView, SessionStatusView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("session/", SessionStatusView.as_view(), name="session-status"),
]

