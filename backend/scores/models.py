from django.db import models

# Create your models here.
from django.db import models

class LiveScore(models.Model):
    match = models.OneToOneField('cricket_statistics.Match', on_delete=models.CASCADE)
    current_batting_team = models.CharField(max_length=50)
    current_bowling_team = models.CharField(max_length=50)
    current_score = models.IntegerField()
    current_wickets = models.IntegerField()
    current_overs = models.DecimalField(max_digits=4, decimal_places=1)
    target = models.IntegerField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Live Score: {self.current_batting_team}"

class BattingScore(models.Model):
    match = models.ForeignKey('cricket_statistics.Match', on_delete=models.CASCADE)
    player = models.ForeignKey('players.Player', on_delete=models.CASCADE)
    runs = models.IntegerField()
    balls = models.IntegerField()
    fours = models.IntegerField()
    sixes = models.IntegerField()
    strike_rate = models.DecimalField(max_digits=5, decimal_places=2)
    out_status = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.player.name} - {self.runs} runs"