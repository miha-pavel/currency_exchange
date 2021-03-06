from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup_d/', views.SignUpDimaView.as_view(), name='signup_d'),
    path('signup_sms/', views.SignUpSMSView.as_view(), name='signup_sms'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('my_profile/<int:pk>/', views.MyProfile.as_view(), name='my_profile'),
    path('activate/<uuid:activation_code>/', views.Activate.as_view(), name='activate'),
    path('confirm_sms/', views.ConfirmSMSCodeView.as_view(), name='confirm_sms'),
]
