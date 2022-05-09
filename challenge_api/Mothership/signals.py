from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
import secrets
from Ship.models import Ship
from helpers.models import Configurations

@receiver(post_save, sender=Ship)
def create_or_update_ship(sender, instance,**kwargs):
    try:
        configuration:int = Configurations.objects.filter().first()
    except Configurations.DoesNotExist():
        return None
    
    ship_objects = []
    counter = 1
    while counter <= configuration.max_ships_to_mothership_capacity:
        _name = random_name_generator()
        if not Ship.object.filter(name=_name).exists:
            ship_objects.append(Ship(name=_name))
            counter +=1
    
    Ship.objects.bulk_create(ship_objects)
