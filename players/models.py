from django.db import models
import datetime

from pydantic import Required

# Player model for players.


class Player(models.Model):
    identifier = models.IntegerField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True)

    '''
    "identifier": 12345,
    "first_name": "Hector",
        "last_name": "Bellerin",
        "team": "Arsenal",
        "position": "Defender",
        "image": "hectorbellerin.jpg"
    '''
