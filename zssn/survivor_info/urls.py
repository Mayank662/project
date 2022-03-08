from django.urls import path
from . import views

urlpatterns = [
    path('survivors', views.survivor_fun, name = 'survivor_insert'),
    path('survivors/<int:id>/',views.survivor_fun, name = 'survivor_update'),
    path('survivors/reports/',views.report, name = 'survivor_report')
]
