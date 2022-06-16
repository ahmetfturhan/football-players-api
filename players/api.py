from ast import Str
from email import message
from typing import List, Optional
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, File
from ninja.files import UploadedFile
from typing import List
from requests import request
from players.models import Player
from players.schema import PlayerInSchema, PlayerOutSchema, NotFoundSchema
from players import services


api = NinjaAPI()


# Retrieve all players
@api.get("/players", response=List[PlayerOutSchema])
def get_players(request):
    return services.getPlayers(request)


# Retrieve a player based on ID. Returns 200 if the player exist.
# Returns 404 along with a NotFoundSchema if the player does not exist.
@api.get("/players/{player_id}", response={200: PlayerOutSchema, 404: NotFoundSchema})
def view_player(request, player_id: int):
    return services.viewPlayer(request, player_id)


# Retrieve the player based on identifier.
@api.get("/players/identifier/{identif}", response={200: PlayerOutSchema, 404: NotFoundSchema})
def view_player_with_identifier(request, identif: int):
    return services.viewPlayerWIdentifier(request, identif)


# Create a player along with a JSON data.
@api.post("/players", response={201: PlayerOutSchema})
def create_player(request, newPlayer: PlayerInSchema):
    return services.createPlayer(request, newPlayer)


# Update an existing player along with a JSON data.
@api.put("/player/{player_id}", response={200: PlayerOutSchema, 404: NotFoundSchema})
def update_player(request, player_id: int, data: PlayerInSchema):
   return services.updatePlayer(request, player_id, data)

# Delete a player based on their ID.
@api.delete("/player/{player_id}", response={200: int, 404: NotFoundSchema})
def delete_player(request, player_id: int):
    return services.deletePlayer(request, player_id)
