from django.urls import path
from . import views

app_name = 'itemfilters'

urlpatterns = [
    path('', views.filter_list, name='filter_list'),
    path('add/', views.add_filter, name='add_filter'),
]