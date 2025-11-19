from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),

    # api 문서
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/", include("api.urls")),

    # path("registerdemo/", TemplateView.as_view(template_name="registerdemo.html")),

    # frontend 템플릿
    path("", include("frontend.urls")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.insert(0, path("__debug__/", include(debug_toolbar.urls)))

# 미디어 파일 (파일 업로드용)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

