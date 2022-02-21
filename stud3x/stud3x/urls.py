"""stud3x URL Configuration"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import index

urlpatterns = [
    # path('api/', include(router.urls)),
    path('addi/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', index)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'stud3x.views.page_not_found_view'