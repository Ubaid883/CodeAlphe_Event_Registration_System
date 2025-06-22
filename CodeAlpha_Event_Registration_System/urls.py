from django.contrib import admin
from django.urls import path
from Event_Management_System.views import home, EventView, RegisterDetailView, RegisterListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('event/', EventView.as_view(),name='event'),
    path('register/', RegisterListView.as_view(),name='register'),
    path('register/<int:pk>/', RegisterDetailView.as_view(),name='register-details'),

]
