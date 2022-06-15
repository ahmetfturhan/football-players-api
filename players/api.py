from ast import Str
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


# Retrieve all players
@api.get("/players", response=List[PlayerSchema])
def getPlayers(request):
    return Player.objects.all()  # return all players


# Retrieve a player based on ID. Returns 200 if the player exist.
# Returns 404 along with a NotFoundSchema if the player does not exist.
@api.get("/players/{player_id}", response={200: PlayerSchema, 404: NotFoundSchema})
def viewPlayer(request, player_id: int):
    try:
        # get the player according to their id
        player = Player.objects.get(pk=player_id)
        return 200, player  # return response 200 and player object
    except Player.DoesNotExist as e:
        return 404, {"message": "Player you are looking for does not exist."}


# Retrieve the player based on identifier.
@api.get("/players/identifier/{identif}", response={200: PlayerSchema, 404: NotFoundSchema})
def viewPlayer(request, identif: int):
    try:
        player = Player.objects.get(identifier=identif)
        return 200, player
    except Player.DoesNotExist as e:
        return 404, {"message": "Player you are looking for does not exist."}


# Create a player along with a JSON data.
@api.post("/players", response={201: PlayerSchema})
def createPlayer(request, newPlayer: PlayerSchema):
    # create the player using the JSON data.
    newPlayer = Player.objects.create(**newPlayer.dict())
    return newPlayer


# Update an existing player along with a JSON data.
@api.put("/player/{player_id}", response={200: PlayerSchema, 404: NotFoundSchema})
def updatePlayer(request, player_id: int, data: PlayerSchema):
    try:
        player = Player.objects.get(pk=player_id)  # get the player object
        # for every attribute in JSON data, set the corresponding fields in Player object.
        for attr, value in data.dict().items():
            setattr(player, attr, value)
        player.save()  # save the changes on DB
        return 200, player
    except Player.DoesNotExist as e:
        return 404, {"message": "Player you are looking for does not exist."}

# Delete a player based on their ID.


@api.delete("/player/{player_id}", response={200: int, 404: NotFoundSchema})
def deletePlayer(request, player_id: int):
    try:
        player = Player.objects.get(pk=player_id)
        player.delete()  # delete the player on DB
        return 200, player_id
    except Player.DoesNotExist as e:
        return 404, {"message": "Player you are looking for does not exist."}
