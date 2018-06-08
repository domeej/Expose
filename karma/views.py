from django.shortcuts import render
from django.http import request
from django.http import HttpResponse
from django.views import generic
from karma.models import Player
# Create your views here.

def index(request):
    return render(request, 'karma/index.html')


class NewGameView(generic.ListView):
    template_name = 'karma/new_game.html'
    context_object_name = 'players'
    print(Player.objects.all())

    def get_queryset(self):
        print(Player.objects.all())
        return Player.objects.all()

