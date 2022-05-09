from rest_framework import serializers
from .models import Mothership


class MotherShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mothership
        
        fields = (
            'id',
            'name'
           
        )