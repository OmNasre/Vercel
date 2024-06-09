from django.contrib import admin
from django.urls import path, include
from aptitudeTest import views

urlpatterns = [
    path('', views.index, name = "aptitudetest"),
]
