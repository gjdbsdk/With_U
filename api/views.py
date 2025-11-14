
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer, CitizenContentSerializer
from django.shortcuts import redirect
from django.views.generic import TemplateView
from rest_framework.parsers import MultiPartParser, FormParser


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

#커뮤니티 글쓰기 로그인 확인
class CheckLoginAPI(APIView):
    def get(self, request):
        return Response({
            "is_authenticated": request.user.is_authenticated
        })
#시민 참여 콘텐츠 제출 api
class CitizenContentUploadAPI(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = CitizenContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user if request.user.is_authenticated else None)
            return Response({"message": "제출 완료!"}, status=201)
        return Response(serializer.errors, status=400)