from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=80)
    mapname = models.CharField(max_length=250)
    maxplayer = models.IntegerField()
    gametype = models.CharField(max_length=60)