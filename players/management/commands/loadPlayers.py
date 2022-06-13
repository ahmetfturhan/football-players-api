from datetime import datetime
import json

from django.conf import settings
from django.core.management.base import BaseCommand

from players.models import Player

class Command(BaseCommand):
    help = 'Create tracks from JSON file'

    def handle(self, *args, **kwargs):
        # set the path to the datafile
        datafile = settings.BASE_DIR / 'footballApp' / 'data' / 'playerData.json'
        print("path", datafile)
        assert datafile.exists()
        # load the datafile
        with open(datafile, 'r') as f:
            data = json.load(f)
        
        # convert list of dictionaries to list of Track models, and bulk_create
        players = [Player(**player) for player in data]

        Player.objects.bulk_create(players)