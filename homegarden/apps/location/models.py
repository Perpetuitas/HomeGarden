#Location Models. At the moment there are only "Rooms", it is planned to 
#expand this to be able to manage whole buildings, to accomondate future
# possible expansions (Bigger HomeGardens or even other devices)

from django.db import models

class Room(models.Model):
    room_name=models.CharField(max_length=200)
    room_note=models.CharField(max_length=1000)
