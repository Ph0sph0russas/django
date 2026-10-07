from datetime import date

from django.test import TestCase
from django.contrib.auth.models import User
from bakugan_tournaments.models import Tournament, Game, Participants_in_game, Application
from model_bakery import baker
# Create your tests here.
class Test(TestCase):
    def test_list(self):
        self.assertEqual(1, 1)
class TournamentsViewsetTest(TestCase):
    def test_get_list(self):
        tournament = Tournament.objects.create(
            name = "Февральский 2024",
            start_date = "2024-02-01",
            end_date = "2024-02-20",
            stages_count = 4,
            g_power_limit = 670,
            rules = "Японские без доклада",
            prize = '500 rub'
        )

        r = self.client.get('/api/tournaments/')
       
        data = r.json()
        print(data)

        assert tournament.id == data[0]['id']
        assert tournament.name == data[0]['name']
        assert tournament.start_date== data[0]['start_date']
        assert tournament.end_date == data[0]['end_date']
        assert tournament.stages_count == data[0]['stages_count']
        assert tournament.g_power_limit == data[0]['g_power_limit']
        assert tournament.rules == data[0]['rules']
        assert tournament.prize == data[0]['prize']
        assert len(data) == 1
    def test_create_tournament(self):
        r = self.client.post("/api/tournaments/", {
            "name": "Февральский 2024",
            "start_date": '2024-02-01',
            "end_date": '2024-02-20',
            "stages_count": 4,
            "g_power_limit": 670,
            "rules": "Японские без доклада",
            "prize": "700 rub"
        })

        new_tournament_id = r.json()['id']

        tournaments = Tournament.objects.all()
        assert len(tournaments)==1

        new_tournament = Tournament.objects.filter(id=new_tournament_id).first()
        
        assert new_tournament.name == 'Февральский 2024'
        assert new_tournament.start_date==  date(2024, 2, 1)
        assert new_tournament.end_date == date(2024, 2, 20)
        assert new_tournament.stages_count == 4
        assert new_tournament.g_power_limit == 670
        assert new_tournament.rules == 'Японские без доклада'
        assert new_tournament.prize == '700 rub'

    
class GameViewsetTest(TestCase):
    def test_get_list(self):
        
        tournament = Tournament.objects.create(
            name="Октябрьский 2026",
            start_date="2026-09-23", 
            end_date="2026-10-31",
            stages_count=5,
            prize="500 рублей",
            g_power_limit=650,
            rules="Европейские с докладом",
        )

       
        game = Game.objects.create(
            place="ТЦ Курумель",
            start_date="2026-09-23",
            end_date="2026-09-23",
            stage=1,
            status="Завершена",
            tournament=tournament  
        )

        
        r = self.client.get('/api/games/')
        data = r.json()
        print(data)

        assert game.id == data[0]['id']
        assert game.place == data[0]['place']
        assert game.start_date == data[0]['start_date']
        assert game.end_date == data[0]['end_date']
        assert game.stage == data[0]['stage']
        assert game.status == data[0]['status']
        assert game.tournament.id == data[0]['tournament']
        assert len(data) == 1
    def test_create_game(self):
        trnmnt = baker.make("bakugan_tournaments.Tournament")

        r = self.client.post("/api/games/", {
            "place":"ТЦ Курумель",
            "start_date": '2026-09-23',
            "end_date": '2026-09-23',
            "stage": 1,
            "status": "Завершена",
            "tournament": trnmnt.id 
        })

        new_game_id = r.json()['id']
        
        games = Game.objects.all()
        assert len(games) == 1

        new_game = Game.objects.filter(id=new_game_id).first()
        
        assert new_game.place == 'ТЦ Курумель'
        assert new_game.start_date== date(2026, 9, 23)
        assert new_game.end_date== date(2026, 9, 23)
        assert new_game.stage==1
        assert new_game.status == 'Завершена'
        assert new_game.tournament== trnmnt
    def test_delete_game(self):
        games = baker.make("bakugan_tournaments.Game", 10)
        r = self.client.get('/api/games/')
        data = r.json()
        assert len(data) == 10
    
        game_id_to_delete = games[3].id
        self.client.delete(f'/api/games/{game_id_to_delete}/')
    
        r = self.client.get('/api/games/')
        data = r.json()
        assert len(data) == 9
    
        assert game_id_to_delete not in [i['id'] for i in data]

class ParticipantsViewsetTest(TestCase): 
    def test_get_list(self):
        
        user = User.objects.create_user(
            username="user_test",
            password="123"
        )

       
        tournament = Tournament.objects.create(
            name="Октябрьский 2026",
            start_date="2026-09-23",
            end_date="2026-10-31",
            stages_count=5,
            prize="500 рублей",
            g_power_limit=650,
            rules="Европейские с докладом",
        )

        
        game = Game.objects.create(
            place="ТЦ Курумель",
            start_date="2026-09-23",
            end_date="2026-09-23",
            stage=1,
            status="Завершена",
            tournament=tournament
        )

        
        participant = Participants_in_game.objects.create(
            team_name="Иркутские",
            win_or_lose=1,  
            game=game,
            user=user
        )
        
       
        r = self.client.get('/api/participants/')
        data = r.json()
      

        assert participant.id == data[0]['id']
        assert participant.team_name == data[0]['team_name']
        assert participant.win_or_lose == data[0]['win_or_lose']
        assert participant.game.id == data[0]['game']
        assert participant.user.id == data[0]['user']
        assert len(data) == 1
    def test_create_participant(self):
        trnmnt = baker.make("bakugan_tournaments.Tournament")
        game = baker.make("bakugan_tournaments.Game", tournament=trnmnt)
        user=baker.make("auth.User")

        r = self.client.post("/api/participants/", {
            "team_name":"Иркутские",
            "win_or_lose": 1,  
            "game": game.id,
            "user": user.id
        })
        new_participant_id = r.json()['id']

        participants=Participants_in_game.objects.all()
        assert len(participants)==1
        new_participant=Participants_in_game.objects.filter(id=new_participant_id).first()

        assert new_participant.team_name == "Иркутские"
        assert new_participant.win_or_lose == 1
        assert new_participant.game == game
        assert new_participant.user == user
    def test_delete_participant(self):
        participants = baker.make("bakugan_tournaments.Participants_in_game", 10)
        r = self.client.get('/api/participants/')
        
        data = r.json()
        assert len(data) == 10

        participant_id_to_delete = participants[3].id
        self.client.delete(f'/api/participants/{participant_id_to_delete}/')
       

        r = self.client.get('/api/participants/')
        data = r.json()
        assert len(data) == 9

        assert participant_id_to_delete not in [i['id'] for i in data]


class ApplicationViewsetTest(TestCase):
    def test_get_list(self):
        
        user = User.objects.create_user(
            username="test_user",
            password="123"
        )

        
        tournament = Tournament.objects.create(
            name="Октябрьский 2026",
            start_date="2026-09-23",
            end_date="2026-10-31",
            stages_count=5,
            prize="500 рублей",
            g_power_limit=650,
            rules="Европейские с докладом",
        )

        
        application = Application.objects.create(
            name="Ph0sph0rus",
            approval=True,          
            tournament=tournament,
            user=user
        )

       
        r = self.client.get('/api/applications/')
        data = r.json()
        print(data)

       
        assert application.id == data[0]['id']
        assert application.name == data[0]['name']
        assert application.approval == data[0]['approval']
        assert application.tournament.id == data[0]['tournament']
        assert application.user.id == data[0]['user']
        assert len(data) == 1
    def test_create_application(self):
        user = baker.make("auth.User")
        trnmnt=baker.make("bakugan_tournaments.Tournament")

        r=self.client.post("/api/applications/", {
            "name":"Ph0sph0rus",
            "approval": 1,          
            "tournament": trnmnt.id,
            "user" : user.id
        })
        new_application_id = r.json()['id']
        applications=Application.objects.all()

        assert len(applications)==1

        new_application = Application.objects.filter(id=new_application_id).first()

        assert new_application.name == 'Ph0sph0rus'
        assert new_application.approval==1
        assert new_application.tournament==trnmnt
        assert new_application.user == user
    def test_delete_application(self):
        applications = baker.make("bakugan_tournaments.Application", 10)
        r = self.client.get('/api/applications/')
        
        data = r.json()
        assert len(data) == 10

        application_id_to_delete = applications[3].id
        self.client.delete(f'/api/applications/{application_id_to_delete}/')
       
        r = self.client.get('/api/applications/')
        
        data = r.json()
        assert len(data) == 9

        assert application_id_to_delete not in [i['id'] for i in data]

