from django.contrib import admin
from django.urls import path
from .import views

app_name = "user"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.userLogin, name="login"),
    path('logout/', views.userLogout, name="logout"),
]
