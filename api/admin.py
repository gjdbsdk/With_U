
from django.contrib import admin
from .models import Project, Post, Comment, CitizenContent


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "created_at")
    search_fields = ("title", "author__username")
    list_filter = ("created_at",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "author", "created_at")
    search_fields = ("post__title", "author__username")


@admin.register(CitizenContent)
class CitizenContentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "category", "created_at")
    search_fields = ("title", "author__username", "category")
    list_filter = ("category", "created_at")
