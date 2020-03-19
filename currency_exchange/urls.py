from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('account/', include('account.urls')),
    path('currency/', include('currency.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]


if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ]\
        + urlpatterns\
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
