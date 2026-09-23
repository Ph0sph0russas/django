from django.contrib import admin
from bakugan_tournaments.models import Tournament, Game, Participants_in_game, Application
# Register your models here.
@admin.register(Tournament)
class TournamentsAdmin(admin.ModelAdmin):
    pass
@admin.register(Game)
class GamesAdmin(admin.ModelAdmin):
    pass
@admin.register(Participants_in_game)
class ParticipantsAdmin(admin.ModelAdmin):
    pass
@admin.register(Application)
class ApplicationsAdmin(admin.ModelAdmin):
    pass