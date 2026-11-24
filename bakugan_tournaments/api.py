from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate

from bakugan_tournaments.models import Tournament, Game, Participants_in_game, Application, Profile
from bakugan_tournaments.serializers import TournamentSerializer, GameSerializer, ParticipantsSerializer, ApplicationSerializer, ProfileSerializer

class TournamentViewset(
    mixins.RetrieveModelMixin, 
    mixins.DestroyModelMixin, 
    mixins.CreateModelMixin, 
    mixins.UpdateModelMixin,
    mixins.ListModelMixin, 
    GenericViewSet
):
    queryset= Tournament.objects.all()
    serializer_class=TournamentSerializer

class GameViewset(
    mixins.RetrieveModelMixin, 
    mixins.DestroyModelMixin, 
    mixins.CreateModelMixin, 
    mixins.UpdateModelMixin,
    mixins.ListModelMixin, 
    GenericViewSet
):
    queryset= Game.objects.all()
    serializer_class=GameSerializer

class ParticipantsViewset(
    mixins.RetrieveModelMixin, 
    mixins.DestroyModelMixin, 
    mixins.CreateModelMixin, 
    mixins.UpdateModelMixin, 
    mixins.ListModelMixin, 
    GenericViewSet
):
    queryset=Participants_in_game.objects.all()
    serializer_class=ParticipantsSerializer

class ApplicationViewset(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset=Application.objects.all()
    serializer_class=ApplicationSerializer
class ProfileViewset(mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    
    queryset=User.objects.all()
    serializer_class=ProfileSerializer

    @action(detail=False, url_path="me", methods=['GET'])
    def get_me(self, request, *args, **kwargs):
        data = {
            'is_authenticated': self.request.user.is_authenticated
        }

        if self.request.user.is_authenticated:
            data.update({
                "username": self.request.user.username,
                "id": self.request.user.id,
                "role": self.request.user.profile.role
            })

        
        return Response(data=data)
    @action(detail=False, url_path="logout", methods=['POST'])
    def logout(self, request, *args, **kwargs):
        django_logout(self.request)
        return Response()

    @action(detail=False, url_path="login", methods=['POST'])
    def login(self, request, *args, **kwargs):
        username=self.request.data['username']
        password=self.request.data['password']
        success = False
        status_code=403
        user= authenticate(username=username, password=password)
        if user:
            success=True
            status_code=200
            django_login(self.request, user)
        

        return Response({
            'success': success
        }, status=status_code)
