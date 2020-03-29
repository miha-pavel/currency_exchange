from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_swagger.views import get_swagger_view


API_PREFIX = 'api/v1'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('account/', include('account.urls')),
    path('currency/', include('currency.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    # API
    path(f'{API_PREFIX}/currency/', include('currency.api.urls')),
    path(f'{API_PREFIX}/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{API_PREFIX}/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


# SWAGGER
schema_view = get_swagger_view(title='DOCS')

urlpatterns.append(path(f'{API_PREFIX}/docs/', schema_view))


if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ]\
        + urlpatterns\
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
