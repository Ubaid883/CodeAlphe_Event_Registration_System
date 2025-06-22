from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import EventSerailizer, RegisterSerializer
from .models import Events, RegistrationModel
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome To Event Management System</h1> ')

class EventView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    #Get all Event's
    def get(self, request):
        query_set = Events.objects.all()
        serailizer = EventSerailizer(query_set, many=True)
        return Response (serailizer.data)
    
    # Create a new Event
    def post(self, request):
        serializer = EventSerailizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        

# Register Event Class based view
class RegisterListView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    # To View The Register
    def get(self, request):
        #get all Registeration data
        data = RegistrationModel.objects.all()
        # convert register data into serailizer
        serializer = RegisterSerializer(data, many=True)
        return Response(serializer.data)
    
    # Create a Register
    def post(self, request):
        serializer = RegisterSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class RegisterDetailView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]   
    # delete particular Register
    def delete(self, request, pk):
        query_set = RegistrationModel.objects.get(pk=pk)
        query_set.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    #get particular Register
    def get_object(self, pk):
        try:
            return RegistrationModel.objects.get(pk=pk)
        except RegistrationModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        registration = self.get_object(pk)
        serializer = RegisterSerializer(registration)
        return Response(serializer.data)