from django.urls import path
from . import views

urlpatterns = [
    path('register', views.AccountCreate.as_view(), name='register'),
    path('login', views.LoginAPIView.as_view(), name='login'),
    path('user', views.UserAPIView.as_view(), name='user'),
    path('refresh', views.RefreshAPIView.as_view(), name='refresh-token'),
    path('logout', views.LogoutAPIView.as_view(), name='logout')
]
