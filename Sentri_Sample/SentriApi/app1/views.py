from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Emissions
from .serializers import EmissionsSerializer



class EmissionsListCreate(generics.ListCreateAPIView):
    queryset = Emissions.objects.all()
    serializer_class = EmissionsSerializer


class EmissionsDetail(generics.RetrieveAPIView):
    queryset = Emissions.objects.all()
    serializer_class = EmissionsSerializer
