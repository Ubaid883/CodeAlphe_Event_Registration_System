from django.contrib import admin
from .models import Events, RegistrationModel
# Register your models here.

#Register Admin
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['Organization_name','event_name']
    
admin.site.register(RegistrationModel, RegisterAdmin)

# Event Admin 
class EventAdmin(admin.ModelAdmin):
   list_display = ['title','description','date','location']
admin.site.register(Events,  EventAdmin)

