from rest_framework import serializers

from bakugan_tournaments.models import Tournament, Game, Participants_in_game, Application, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields="__all__"
class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields=['id', 'name', 'start_date', 'end_date', 'stages_count', 'prize', 'g_power_limit', 'rules', 'preview']

class GameSerializer(serializers.ModelSerializer):
    tournament_instance = TournamentSerializer(read_only=True, source='tournament')

    class Meta:
        model = Game
        fields=['id', 'tournament', 'tournament_instance', 'place', 'start_date', 'end_date', 'stage', 'status']

class ApplicationSerializer(serializers.ModelSerializer):
    tournament_instance=TournamentSerializer(read_only=True, source='tournament')
    class Meta:
        model = Application
        fields=['id', 'name', 'team_name', 'tournament', 'tournament_instance', 'approval', 'user', 'picture']

class ParticipantsSerializer(serializers.ModelSerializer):
    application_instance=ApplicationSerializer(read_only=True, source='application')
    game_instance = GameSerializer(read_only=True, source='game')
    class Meta:
        model = Participants_in_game
        fields=['id', 'game', 'game_instance', 'application', 'application_instance', 'win_or_lose']

