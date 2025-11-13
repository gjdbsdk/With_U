from django.contrib import admin
from .models import CitizenContent

@admin.register(CitizenContent)
class CitizenContentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "author", "created_at")
    search_fields = ("title", "category", "author__username")
    list_filter = ("category", "created_at")