from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    path('smoke/', views.smoke, name='smoke'),
]
