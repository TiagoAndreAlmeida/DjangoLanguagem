from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response

from .models import Languagem
from .serializers import LanguagemSerializers

# Create your views here.
class LanguagemViews(viewsets.ModelViewSet):
    queryset = Languagem.objects.all()
    serializer_class = LanguagemSerializers

    @api_view(['post'])
    def createLanguagem(self, request, *args, **kwargs):
        
        _name = request.data.get('name','')
        _paradigm = request.data.get('paradigm','')

        new = Languagem(
            name = _name,
            paradigm = _paradigm
        )
        new.save()
        res = {'name': _name, 'paradigm': _paradigm}
        return Response(res, status=status.HTTP_200_OK)
    