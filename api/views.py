from django.shortcuts import render
from rest_framework import viewsets

from .models import Languagem
from .serializers import LanguagemSerializers

# Create your views here.
class LanguagemViews(viewsets.ModelViewSet):
    queryset = Languagem.objects.all()
    serializer_class = LanguagemSerializers