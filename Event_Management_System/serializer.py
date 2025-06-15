from rest_framework import serializers
from .models import Events, Registration
class EventSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
class RegistraionSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields  = '__all__'
        