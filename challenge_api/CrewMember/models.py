from django.db import models
from helpers.models import BaseAbstractModel




class CrewMember(BaseAbstractModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.name
# Create your models here.
