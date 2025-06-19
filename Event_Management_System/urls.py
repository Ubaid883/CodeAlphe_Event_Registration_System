from .views import EventView, RegisterView, home
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('register',RegisterView.as_view(), name='register'),
    path('event',EventView.as_view(), name='register'),
    path('register/<int:pk>/',RegisterView.as_view())

    
    
]


