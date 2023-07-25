from django.urls import path
from . import views

urlpatterns = [
    path('home', views.demo),
    path('login', views.login),
    path('table', views.tableDemo),
]
