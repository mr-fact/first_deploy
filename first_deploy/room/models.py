from textwrap import dedent

from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField(default=1403)
    capacity = models.IntegerField(default=6)

    def __str__(self):
        return str(self.name)


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='students')
    year = models.IntegerField(default=1403)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='students', blank=True, null=True, default=None)

    def __str__(self):
        return str(self.user.username)
