# events/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.event_list, name='event_list'),
    path('create/', views.event_create, name='event_create'),
    path('edit/<int:pk>/', views.event_edit, name='event_edit'),
    path('delete/<int:pk>/', views.event_delete, name='event_delete'),
]
