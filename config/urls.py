from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/", include("api.urls")),

    # registerdemo는 frontend보다 위에 있어야 가로채이지 않음
    path("registerdemo/", TemplateView.as_view(template_name="registerdemo.html")),

    # frontend는 항상 가장 아래
    path("", include("frontend.urls")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.insert(0, path("__debug__/", include(debug_toolbar.urls)))

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns.insert(0, path("__debug__/", include(debug_toolbar.urls)))

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)