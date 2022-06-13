from email import message
from typing import List, Optional
from ninja import NinjaAPI, File 
from ninja.files import UploadedFile
from typing import List
from requests import request
from players.models import Player
from players.schema import PlayerSchema, NotFoundSchema

api = NinjaAPI()

@api.get("/players", response=List[PlayerSchema])
def getPlayers(request):
    return Player.objects.all()
