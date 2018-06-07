from django.contrib import admin
from .models import Player, Game, Alias, Rank

# Register your models here.

admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Alias)
admin.site.register(Rank)

