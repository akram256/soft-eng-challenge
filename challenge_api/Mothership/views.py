from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import MotherShipSerializer
from .models import Mothership
from Ship.models import Ship


# Create your views here.

class MothershipView(ListAPIView):
    serializer_class=MotherShipSerializer
    permission_classes=(AllowAny,)
    queryset= Mothership.objects.all()

    def post(self, request):
       
        post_data = {"name":request.data["name"]}
        serializer = self.get_serializer(data=post_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        Ship.objects.bulk_create(
            [Ship(name=""),
            Ship(name=""),
            Ship(name= "")]
            )

        
        return Response({"message":"MotherShip has been  successfully created"},
                        status=status.HTTP_201_CREATED)