from rest_framework import serializers
from .models import Events, RegistrationModel

# Event Serailizer
class EventSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
# Register Serailizer 
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationModel
        fields = '__all__'
