from django.shortcuts import render
from players.models import Player
# Create your views here.
def index(request):
    return render(request, 'index.html', {})
def playerDetail(request):
    return render(request, 'playerDetail.html', {})

def playerDetail(request, player_id:int):
    data = Player.objects.filter(pk=player_id)

    player = {
       "Player": data
    }
    return render(request, "playerDetail.html", player)

