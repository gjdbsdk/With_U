# api/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CitizenContent

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
    
    # 이메일 중복 검사
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("이미 사용 중인 이메일입니다.")
        return value
    
    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )

#시민공유 콘텐츠 제출 api
class CitizenContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenContent
        fields = [
            "id",
            "title",
            "category",
            "content",
            "file",
            "author",
            "created_at",
        ]
        read_only_fields = ["id", "author", "created_at"]