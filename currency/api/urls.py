from django.urls import path

from . import views

app_name = 'api-currency'

urlpatterns = [
    path('rates/', views.RatesView.as_view(), name='rates'),
    path('rates/<int:pk>/', views.RateView.as_view(), name='rate'),
    path('rates/source/<int:source_pk>/', views.RatesSourceView.as_view(), name='rates_source'),
    path('rates/currency/<int:currency_pk>/', views.RatesCurrencyView.as_view(), name='rates_currency'),
    path('rates/created/', views.CreatedFilterView.as_view(), name='rates_created'),
]
