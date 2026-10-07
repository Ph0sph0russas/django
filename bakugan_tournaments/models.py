from django.db import models
from django.conf import settings

# Create your models here.
class Tournament(models.Model):
    name = models.TextField("Название")
    start_date = models.DateField("Дата начала")
    end_date = models.DateField("Дата окончания")
    stages_count = models.IntegerField("Количество стадий")
    prize = models.TextField("Приз")
    g_power_limit = models.IntegerField("Ограничение силы")
    rules=models.TextField("Правила")

    def __str__(self) -> str:
        return self.name
class Game(models.Model):
    tournament=models.ForeignKey("tournament", on_delete=models.CASCADE, null=True)
    place = models.TextField("Место проведения")
    start_date = models.DateField("Дата начала")
    end_date = models.DateField("Дата окончания")
    stage = models.IntegerField("Стадия")
    status=models.TextField("Статус")

    def __str__(self) -> str:
        return str(self.tournament) + " Стадия " + str(self.stage)
class Participants_in_game(models.Model):
    game=models.ForeignKey("game", on_delete=models.CASCADE, null=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    team_name=models.TextField("Название команды")
    win_or_lose=models.BooleanField("Победа/поражение")
    
    def __str__(self) -> str:
        return str(self.user) + " " + str(self.game) + " " + self.team_name
class Application(models.Model):
    name=models.TextField("Имя")
    tournament = models.ForeignKey("tournament", on_delete=models.CASCADE, null=True)
    approval = models.BooleanField("Одобрение")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name + " " + str(self.tournament)
