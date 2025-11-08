from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

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
    path("", include("frontend.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.insert(0, path("__debug__/", include(debug_toolbar.urls)))

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

