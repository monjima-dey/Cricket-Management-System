from django.db import models

# Create your models here.
from django.db import models

class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    match_date = models.DateTimeField()
    venue = models.CharField(max_length=100)
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
    match_type = models.CharField(max_length=20)  # T20, ODI, Test
    status = models.CharField(max_length=20)  # Live, Completed, Upcoming
    result = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.team1} vs {self.team2} - {self.match_date.date()}"

class MatchStatistics(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    innings = models.IntegerField()
    total_runs = models.IntegerField()
    wickets = models.IntegerField()
    overs = models.DecimalField(max_digits=4, decimal_places=1)
    extras = models.IntegerField()
    run_rate = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"Match {self.match.match_id} - Innings {self.innings}"