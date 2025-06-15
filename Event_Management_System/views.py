from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import EventSerailizer, RegistraionSerailizer
from .models import Events, Registration

# Create your views here.
# View End Point
@api_view()
def view_event(request):
    #gets all Events
    data = Events.objects.all()
    # Convert Serailizer int Json
    serailizer = EventSerailizer(data, many=True)
    return Response(serailizer.data)

# Register Event End point
@api_view()
def register_event(request):
    #get all register data
    data = Registration.objects.all()
    #Convert Serializer data into Json
    serailizer = RegistraionSerailizer(data, many=True)
    return Response(serailizer.data)
    
    
    