from .views import view_event
from django.urls import path

urlpatterns = [
    path('', view_event, name='event'),

    
    
]


