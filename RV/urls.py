from django.urls import path
from .views import *


urlpatterns = [
    path('', views.home),
    path('login/', views.login_page),
    path('register/', views.register),
]