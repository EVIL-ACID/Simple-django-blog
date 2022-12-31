
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')), # The CKEditor path
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Path for media files
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
