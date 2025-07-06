from django.urls import path
from . import views

app_name = 'itemfilters'

urlpatterns = [
    path('', views.filter_list, name='filter_list'),
    path('add/', views.add_filter, name='add_filter'),
    path('<int:pk>/edit/', views.edit_filter, name='edit_filter'),
    path('<int:pk>/delete/', views.delete_filter, name='delete_filter'),
]