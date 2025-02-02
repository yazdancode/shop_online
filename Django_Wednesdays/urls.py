from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("grappelli/", include("grappelli.urls")),
    path("", include("store.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         re_path(r'^__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
