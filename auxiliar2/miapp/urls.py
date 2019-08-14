from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('equipo/', views.equipo, name='equipo'),
    path('libre/', views.libre, name='libre')
]