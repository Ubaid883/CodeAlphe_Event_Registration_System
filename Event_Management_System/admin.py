from django.contrib import admin
from .models import Events, RegistrationModel
# Register your models here.
# Event Admin 
class EventAdmin(admin.ModelAdmin):
    list_display = ('title','description','date','location')
admin.site.register(Events,  EventAdmin)

#Register Admin
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['name','event', 'date']
admin.site.register(RegistrationModel, RegisterAdmin)