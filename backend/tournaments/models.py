from django.db import models

# Create your models here.
from django.db import models

class Tournament(models.Model):
    tournament_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    format = models.CharField(max_length=20)  # T20, ODI, Test
    status = models.CharField(max_length=20)  # Upcoming, Ongoing, Completed
    description = models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    captain = models.ForeignKey('players.Player', on_delete=models.SET_NULL, null=True, related_name='captain_of')
    players = models.ManyToManyField('players.Player', related_name='team_players')
    points = models.IntegerField(default=0)
    matches_played = models.IntegerField(default=0)

    def __str__(self):
        return self.name