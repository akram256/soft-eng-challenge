from django.db import models
from helpers.models import BaseAbstractModel

# Create your models here.




class Mothership(BaseAbstractModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.name
    

