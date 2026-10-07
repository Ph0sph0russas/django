from rest_framework import serializers

from bakugan_tournaments.models import Tournament, Game, Participants_in_game, Application

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields=['id', 'name', 'start_date', 'end_date', 'stages_count', 'prize', 'g_power_limit', 'rules']

class GameSerializer(serializers.ModelSerializer):
    tournament_instance = TournamentSerializer(read_only=True, source='tournament')

    class Meta:
        model = Game
        fields=['id', 'tournament', 'tournament_instance', 'place', 'start_date', 'end_date', 'stage', 'status']

class ParticipantsSerializer(serializers.ModelSerializer):
    game_instance = GameSerializer(read_only=True, source='game')
    class Meta:
        model = Participants_in_game
        fields=['id', 'game', 'game_instance', 'team_name', 'win_or_lose', 'user']

class ApplicationSerializer(serializers.ModelSerializer):
    tournament_instance=TournamentSerializer(read_only=True, source='tournament')
    class Meta:
        model = Application
        fields=['id', 'name', 'tournament', 'tournament_instance', 'approval', 'user']