from rest_framework import serializers
from .models import Languagem

class LanguagemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Languagem
        fields = '__all__'