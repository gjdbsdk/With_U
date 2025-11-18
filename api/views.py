from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic import TemplateView


from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import RegisterSerializer, CitizenContentSerializer
from .models import Post, CitizenContent, Comment

# 회원가입
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

# 로그인
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"message": "아이디와 비밀번호를 모두 입력해주세요."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response(
                {"message": "아이디 또는 비밀번호가 올바르지 않습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        login(request, user)  # 세션 로그인
        return Response({"message": "로그인 성공", "username": username})

# 로그아웃
class LogoutView(APIView):
    def post(self, request):
        logout(request)  # 세션 삭제
        return Response({"message": "로그아웃 성공"}, status=status.HTTP_200_OK)



#시민 참여 콘텐츠 제출 api 
#    POST /api/citizen/upload/
class CitizenContentUploadAPI(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        # 시민참여는 로그인한 사용자만 가능하게 - 이부분 충돌날겁니다...
        if not request.user.is_authenticated:
            return Response(
                {"message": "로그인이 필요합니다."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        serializer = CitizenContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response({"message": "제출 완료!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
# 커뮤니티 글쓰기
#    POST /api/post/create/
#    writing.html에서 fetch로 호출하면 됨
class CreatePostAPI(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            return Response(
                {"message": "로그인이 필요합니다."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        title = request.data.get("title", "").trim() if hasattr(str, "trim") else request.data.get("title", "").strip()
        content = request.data.get("content", "").strip()

        if not title or not content:
            return Response(
                {"message": "제목과 내용을 모두 입력해주세요."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        Post.objects.create(
            author=request.user,
            title=title,
            content=content,
        )

        return Response({"message": "게시글 작성 성공"}, status=status.HTTP_201_CREATED)

# 7) 댓글 작성 API (필요 시 사용)
#    POST /api/comment/<post_id>/create/

class CreateCommentAPI(APIView):
    def post(self, request, post_id):
        if not request.user.is_authenticated:
            return Response(
                {"message": "로그인이 필요합니다."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        content = request.data.get("content", "").strip()
        if not content:
            return Response(
                {"message": "댓글 내용을 입력해주세요."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        post = get_object_or_404(Post, id=post_id)

        Comment.objects.create(
            post=post,
            author=request.user,
            content=content,
        )

        return Response({"message": "댓글 작성 성공"}, status=status.HTTP_201_CREATED)

# 좋아요 토글 API
#    POST /api/like/<post_id>/
#    community.js 에서 fetch로 호출

class LikePostAPI(APIView):
    def post(self, request, post_id):
        if not request.user.is_authenticated:
            return Response(
                {"detail": "login_required"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        post = get_object_or_404(Post, id=post_id)

        if request.user in post.likes.all():
            post.likes.remove(request.user)
            action = "unliked"
        else:
            post.likes.add(request.user)
            action = "liked"

        return Response(
            {
                "action": action,
                "likes_count": post.likes.count(),
            }
        )
    
# 로그인 여부 체크
class CheckLoginAPIView(APIView):
    # 프론트에서 /api/check-login/으로 로그인 여부 확인
    def get(self, request):
        return Response({"is_authenticated": request.user.is_authenticated})