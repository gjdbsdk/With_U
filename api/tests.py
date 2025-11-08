from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Project


class ProjectViewSetTests(APITestCase):
    def test_create_project(self) -> None:
        url = reverse("project-list")
        payload = {"name": "테스트 프로젝트", "description": "API 흐름 검증"}
        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.first().name, payload["name"])

