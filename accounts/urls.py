from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('verify-phone/', views.CheckTopView.as_view(), name='check_otp'),
    path('login/', views.LoginView.as_view(), name='login'),
]
