from django.contrib import admin
from django.urls import path , include
from django.conf.urls.i18n import i18n_patterns
from .scheme import swagger_urlpatterns
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('i18n/', include("django.conf.urls.i18n"))
]

urlpatterns += i18n_patterns(path("admin/",admin.site.urls))

urlpatterns += swagger_urlpatterns


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
