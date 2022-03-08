from django.urls import path
from . import views

urlpatterns = [
    path('survivors', views.survivor_fun, name = 'survivor_insert'),
    path('<int:id>/',views.survivor_fun, name = 'survivor_update'),
#    path('list/',views.survivor_list, name = 'survivor_list')
]
