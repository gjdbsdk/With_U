
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # 세션 로그인
            return Response({"message": "로그인 성공", "username": username})

        return Response({"message": "아이디 또는 비밀번호가 올바르지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        logout(request)  # 세션 삭제
        return Response({"message": "로그아웃 성공"}, status=status.HTTP_200_OK)