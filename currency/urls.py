from django.urls import path

from . import views


urlpatterns = [
    path('rate_list/', views.RateList.as_view(), name='rate_list'),
]
