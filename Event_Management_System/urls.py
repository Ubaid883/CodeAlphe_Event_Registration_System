from .views import view_event, RegisterView, home
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('event', view_event, name='event'),
    path('register',RegisterView.as_view(), name='register')

    
    
]


