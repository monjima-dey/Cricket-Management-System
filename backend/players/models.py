from django.db import models

# Create your models here.
from django.db import models

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    player_type = models.CharField(max_length=50)  # Batsman, Bowler, All-rounder
    batting_style = models.CharField(max_length=50)
    bowling_style = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='players/', blank=True, null=True)

    def __str__(self):
        return self.name

class PlayerStatistics(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    matches_played = models.IntegerField(default=0)
    runs_scored = models.IntegerField(default=0)
    batting_average = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    wickets_taken = models.IntegerField(default=0)
    bowling_average = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"Statistics for {self.player.name}"