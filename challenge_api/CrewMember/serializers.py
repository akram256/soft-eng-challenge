from rest_framework import serializers
from .models import CrewMember


class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrewMember
        fields = (
            'id',
            'name'
           
        )