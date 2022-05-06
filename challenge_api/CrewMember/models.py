from django.db import models
from helpers.models import BaseAbstractModel
from Ship.models import Ship




class CrewMember(BaseAbstractModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    ship = models.ForeignKey(Ship,on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name
# Create your models here.
