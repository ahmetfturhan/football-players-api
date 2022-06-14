from email import message
from typing import List, Optional
from django.shortcuts import get_object_or_404
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


@api.get("/players/{player_id}", response={200: PlayerSchema, 404: NotFoundSchema})
def viewPlayer(request, player_id: int):
    try:
        player = Player.objects.get(pk=player_id)
        return 200, player
    except Player.DoesNotExist as e:
        return 404, {"message", "Player you are looking for does not exist."}


@api.get("/players/identifier/{identif}", response={200: List[PlayerSchema], 404: NotFoundSchema})
def viewPlayer(request, identif: int):
    try:
        player = Player.objects.filter(identifier=identif)
        return 200, player
    except Player.DoesNotExist as e:
        return 404, {"message", "Player you are looking for does not exist."}
