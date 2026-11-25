from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    class Role(models.IntegerChoices):
        undefined = 0
        organizer = 1
        participant = 2
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, null=True, blank=True)
    role = models.IntegerField("Роль", choices=Role, default=Role.undefined)

    def __str__(self):
        return self.user.username if self.user else f"Profile {self.id}"

@receiver(post_save, sender=User)
def on_user_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance, role=Profile.Role.undefined)


class Tournament(models.Model):
    name = models.TextField("Название")
    start_date = models.DateField("Дата начала")
    end_date = models.DateField("Дата окончания")
    stages_count = models.IntegerField("Количество стадий")
    prize = models.TextField("Приз")
    g_power_limit = models.IntegerField("Ограничение силы")
    rules=models.TextField("Правила")
    preview = models.ImageField("Превью", null=True, upload_to="tournaments")
    
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


class Application(models.Model):
    name=models.TextField("Имя")
    tournament = models.ForeignKey("tournament", on_delete=models.CASCADE, null=True)
    approval = models.BooleanField("Одобрение")
    team_name=models.TextField("Название команды", null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    picture = models.ImageField("Изображение", null=True, upload_to="applications")

    def __str__(self) -> str:
        return self.name + " " + str(self.tournament)

class Participants_in_game(models.Model):
    application = models.ForeignKey("application", on_delete=models.CASCADE, null=True)
    game=models.ForeignKey("game", on_delete=models.CASCADE, null=True)
    win_or_lose=models.BooleanField("Победа/поражение")
    
    def __str__(self) -> str:
        return str(self.user) + " " + str(self.game)

