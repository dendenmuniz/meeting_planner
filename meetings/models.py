from datetime import time
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=200)
    floor_number = models.IntegerField(default=1)
    room_number = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} is locate on {self.floor_number} at {self.room_number}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    participants = models.ManyToManyField(get_user_model())

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
