"""
URL configuration for CodeAlpha_Event_Registration_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Event_Management_System.views import home, EventView, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('event/', EventView.as_view(),name='event'),
    path('register/', RegisterView.as_view(),name='register')
]
