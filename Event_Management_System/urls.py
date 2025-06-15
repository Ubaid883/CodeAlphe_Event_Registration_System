from .views import view_event, register_event
from django.urls import path

urlpatterns = [
    path('', view_event, name='event'),
    path('', register_event, name='register'),
    
    
]


