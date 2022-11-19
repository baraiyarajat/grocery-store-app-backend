from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.AccountCreate.as_view(), name='register'),
]
