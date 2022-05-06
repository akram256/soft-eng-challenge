from django.db import models

from helpers.models import BaseAbstractModel
from Mothership.models import Mothership


# Create your models here.


class Ship(BaseAbstractModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    mothership =  models.ForeignKey(Mothership, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name
