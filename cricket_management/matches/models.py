from django.db import models
from teams.models import Team

class Match(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    match_date_time = models.DateTimeField()
    venue = models.CharField(max_length=200)
    series = models.CharField(max_length=100, blank=True, null=True)
    winner = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='winning_matches')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.team1.name} vs {self.team2.name} at {self.venue} on {self.match_date_time}"