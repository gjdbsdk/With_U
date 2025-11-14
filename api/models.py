from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.name

#커뮤니티 게시글 모델
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 글쓴이 (User 연결)
    title = models.CharField(max_length=200)                    # 제목
    content = models.TextField()                                # 본문
    created_at = models.DateTimeField(auto_now_add=True)        # 작성 시간

    def __str__(self):
        return self.title

    # 템플릿 계산 필드

    @property
    def author_initial(self):
        # 글쓴이 이름(아이디) 첫 글자
        return self.author.username[0]

    @property
    def author_name(self):
        # 글쓴이 전체 이름 → 여기선 username 사용
        return self.author.username

    @property
    def snippet(self):
        # 본문 미리보기 (100자)
        text = self.content
        return text[:100] + "..." if len(text) > 100 else text

    @property
    def detail_url(self):
        # 글 상세 페이지 URL (나중에 진짜 detail 뷰 변경)
        return f"/community/{self.id}/"

#시민참여 콘텐츠 - 파일 업로드 지원, 작성자 정보 저장
class CitizenContent(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(upload_to="citizen_files/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title