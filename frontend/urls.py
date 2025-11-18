from django.urls import path

from . import views

app_name = "frontend"

urlpatterns = [
    path("citizen/", views.CitizenView.as_view(), name="citizen"),
    path("community/", views.CommunityView.as_view(), name="community"),
    # 커뮤니티 상세 페이지
    # <int:post_id> 부분이 URL에 적힌 숫자를 받아 view.spy의 post_detail_view 함수의 post_id 인자로 념겨줌
    path("community/<int:post_id>/", views.post_detail_view, name="post_detail"),
    path("writing/", views.WritingView.as_view(), name="writing"),

    path("emotional/", views.EmotionalView.as_view(), name="emotional"),
    path("health/", views.HealthView.as_view(), name="health"),
    path("", views.HomeView.as_view(), name="home"),
    path("lifestyle/", views.LifestyleView.as_view(), name="lifestyle"),
    path("local/", views.LocalView.as_view(), name="local"),
    path("society/", views.SocietyView.as_view(), name="society"),

    # 회원가입 데모 페이지
    path("registerdemo/", views.RegisterDemoView.as_view(), name="registerdemo"),
    # 로그인 데모 페이지
    path("logindemo/", views.LoginDemoView.as_view(), name="logindemo"),
    path("detail/", views.DetailView.as_view(), name="detail"),
    
]

