from ast import Str
from email import message
from telnetlib import PRAGMA_HEARTBEAT
from typing import List, Optional
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, File
from ninja.files import UploadedFile
from typing import List
from requests import request
from players.models import Player
from players.schema import PlayerInSchema, PlayerOutSchema, NotFoundSchema
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse

def getPlayers(request):
    return Player.objects.all()


def viewPlayer(request, player_id: int):
    try:
        # get the player according to their id
        player = Player.objects.get(pk=player_id)
        return 200, player  # return response 200 and player object
    except Player.DoesNotExist as e:
        return 404, {"message": "Player you are looking for does not exist."}


def viewPlayerWIdentifier(request, identif: int):
    try:
        player = Player.objects.filter(identifier=identif)
        
        # playerList = []
        # for PlayerObject in player:
        #     playerList.append(PlayerObject)
        # # print("sadenemeeeeeeee", playerList)
        serializedPlayer = serializers.serialize('json', player)
        # JsonResponse(serializedPlayer, safe=False)
        # serializedPlayer = serializedPlayer[1:-1]
        # print("sadasdfasdasdasdas",serializedPlayer)
        return 200,JsonResponse(player, safe=False)
    except Player.DoesNotExist as e:
        return 404, {"message": "Player you are looking for does not exist."}


def createPlayer(request, newPlayer: PlayerInSchema):
    # create the player using the JSON data.
    newPlayer = Player.objects.create(**newPlayer.dict())
    return newPlayer


def updatePlayer(request, player_id: int, data: PlayerInSchema):
    try:
        player = Player.objects.get(pk=player_id)  # get the player object
        # for every attribute in JSON data, set the corresponding fields in Player object.
        for attr, value in data.dict().items():
            setattr(player, attr, value)
        player.save()  # save the changes on DB
        return 200, player
    except Player.DoesNotExist as e:
        return 404, {"message": "Player you are looking for does not exist."}


def deletePlayer(request, player_id: int):
    try:
        player = Player.objects.get(pk=player_id)
        player.delete()  # delete the player on DB
        return 200, player_id
    except Player.DoesNotExist as e:
        return 404, {"message": "Player you are looking for does not exist."}
