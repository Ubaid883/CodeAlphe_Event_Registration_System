from rest_framework import serializers
from .models import Events,RegistrationModel

# Event Serailizer
class EventSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
        
        def date_validator(self, data):
            if data['date'] == data['date']:
                raise serializers.ValidationError ('date must be different')
            return data
        
# Register Serailizer 
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationModel
        fields = '__all__'
