from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import EventSerailizer
from .models import Events 

# Create your views here.
@api_view()
def view_event(request):
    #gets all Events
    data = Events.objects.all()
    # Convert Serailizer int Json
    serailizer = EventSerailizer(data, many=True)
    return Response(serailizer.data)
    