from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
