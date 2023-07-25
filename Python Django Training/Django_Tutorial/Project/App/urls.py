from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.demo, name='home')
]
