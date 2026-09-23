from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, viewsets

from bakugan_tournaments.models import Tournament, Game, Participants_in_game, Application
from bakugan_tournaments.serializers import TournamentSerializer, GameSerializer, ParticipantsSerializer, ApplicationSerializer
class TournamentViewset(mixins.ListModelMixin, GenericViewSet):
    queryset= Tournament.objects.all()
    serializer_class=TournamentSerializer

class GameViewset(mixins.ListModelMixin, GenericViewSet):
    queryset= Game.objects.all()
    serializer_class=GameSerializer

class ParticipantsViewset(mixins.ListModelMixin, GenericViewSet):
    queryset=Participants_in_game.objects.all()
    serializer_class=ParticipantsSerializer

class ApplicationViewset(mixins.ListModelMixin, GenericViewSet):
    queryset=Application.objects.all()
    serializer_class=ApplicationSerializer
