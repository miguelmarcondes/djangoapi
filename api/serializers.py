from rest_framework import serializers
from .models import Culprit

class CulpritSerializer(serializers.ModelSerializer):
    class Meta:
        model = Culprit
        fields = '__all__'