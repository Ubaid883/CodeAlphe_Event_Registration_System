from django.contrib import admin
from .models import Events, Registration
# Register your models here.
# Event Admin 
class EventAdmin(admin.ModelAdmin):
    list_display = ('title','description','date','location')
admin.site.register(Events,  EventAdmin)

#Register Admin
class RegiserAdmin(admin.ModelAdmin):
    list_display = ['user','event','register_at']

admin.site.register(Registration, RegiserAdmin)