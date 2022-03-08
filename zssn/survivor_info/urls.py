from django.urls import path, include
from . import views

urlpatterns = [
    path('survivors', views.survivor_fun)
]
