from django.urls import path

from . import views

app_name = "frontend"

urlpatterns = [
    path("citizen/", views.CitizenView.as_view(), name="citizen"),
    path("community/", views.CommunityView.as_view(), name="community"),
    path("emotional/", views.EmotionalView.as_view(), name="emotional"),
    path("health/", views.HealthView.as_view(), name="health"),
    path("", views.HomeView.as_view(), name="home"),
    path("lifestyle/", views.LifestyleView.as_view(), name="lifestyle"),
    path("local/", views.LocalView.as_view(), name="local"),
    path("society/", views.SocietyView.as_view(), name="society"),
]

