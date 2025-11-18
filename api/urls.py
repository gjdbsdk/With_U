
from django.urls import path
from .views import (
    RegisterView, 
    LoginView, 
    LogoutView, 
    CitizenContentUploadAPI, 
    CreatePostAPI,
    CreateCommentAPI,
    LikePostAPI,
    CheckLoginAPIView
)

urlpatterns = [
    # 회원가입/ 로그인/ 로그아웃
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # 로그인 여부 확인
    path("check-login/", CheckLoginAPIView.as_view()),
    # 시민 참여 콘텐츠
    path("citizen/upload/", CitizenContentUploadAPI.as_view()),
    # 커뮤니티 글쓰기
    path("community/write/", CreatePostAPI.as_view()),
    # 댓글 작성
    path("comment/<int:post_id>/create/", CreateCommentAPI.as_view()),
    # 좋아요 토글
    path("community/like/<int:post_id>/", LikePostAPI.as_view(), name="like_post"),
    # 로그인 여부 확인
    path("check-login/", CheckLoginAPIView.as_view(), name="check-login"),
]

