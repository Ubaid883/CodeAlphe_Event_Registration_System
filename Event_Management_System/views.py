from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import EventSerailizer, RegisterSerializer
from .models import Events, RegistrationModel
from rest_framework.views import APIView

# Create your views here.
# View End Point
@api_view()
def view_event(request):
    #gets all Events
    data = Events.objects.all()
    # Convert Serailizer int Json
    serailizer = EventSerailizer(data, many=True)
    return Response(serailizer.data)

# Register Event Class based view
class RegisterView(APIView):
    def get(self, request):
        #get all Registeration data
        data = RegistrationModel.objects.all()
        # convert register data into serailizer
        serializer = RegisterSerializer(data, many=True)
        return Response(serializer.data)

    
    
    