from django.urls import path

from . import views


urlpatterns = [
    path('rate_list/', views.RateList.as_view(), name='rate_list'),
    path('rate_csv/', views.RateCSV.as_view(), name='rate_csv'),
    path('latest_rates/', views.LatestRate.as_view(), name='latest_rates'),
]
