from django.shortcuts import render
from rest_framework import generics
from .models import BaseModel
from .serializes import BaseSerial
# Create your views here.
class BaseAPIView(generics.ListAPIView):
    queryset = BaseModel.objects.all()
    serializer_class = BaseSerial