
# events/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_event, name='add_event'),
    path('', views.event_list, name='event_list'),
]
