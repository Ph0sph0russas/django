from rest_framework import serializers

from bakugan_tournaments.models import Tournament, Game, Participants_in_game, Application

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields=['id', 'name', 'start_date', 'end_date', 'stages_count', 'prize', 'g_power_limit', 'rules']

class GameSerializer(serializers.ModelSerializer):
    tournament=TournamentSerializer()

    class Meta:
        model = Game
        fields=['id', 'tournament', 'start_date', 'end_date', 'stage', 'status']

class ParticipantsSerializer(serializers.ModelSerializer):
    game = GameSerializer()
    class Meta:
        model = Participants_in_game
        fields=['id', 'game', 'team_name', 'win_or_lose']

class ApplicationSerializer(serializers.ModelSerializer):
    tournament=TournamentSerializer()
    class Meta:
        model = Application
        fields=['id', 'tournament', 'approval']