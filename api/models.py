# api/models.py
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


# 커뮤니티 게시글 모델

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # 좋아요 기능 추가
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)

    def __str__(self):
        return self.title

    @property # 작성자 이름 첫 글자
    def author_initial(self):
        return self.author.username[0]

    @property
    def author_name(self):
        return self.author.username

    # 목록 미리보기 100자
    @property
    def snippet(self): 
        text = self.content
        return text[:100] + "..." if len(text) > 100 else text

    # 좋아요 개수
    @property
    def likes_count(self):
        return self.likes.count()

    @property
    def comments_count(self):
        return self.comments.count()
    
    # community.html에서 {{ post.detail_url }} 사용
    @property
    def detail_url(self):
        return f"/community/{self.id}/"


# 댓글 모델 추가

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",  # 위에서 comments_count에 쓰임
    )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def author_initial(self):
        username = self.author.username if self.author else ""
        return username[0] if username else ""

    @property
    def author_name(self):
        return self.author.username if self.author else ""

    def __str__(self):
        return f"{self.author.username} - {self.post.title}"

# 시민참여 콘텐츠 모델

class CitizenContent(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(upload_to="citizen_files/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
