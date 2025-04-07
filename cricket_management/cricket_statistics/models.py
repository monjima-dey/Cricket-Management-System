from django.db import models
from matches.models import Match
from players.models import Player

class PlayerMatchStats(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='player_stats')
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='match_stats')
    runs_scored = models.IntegerField(default=0)
    balls_faced = models.IntegerField(default=0)
    fours = models.IntegerField(default=0)
    sixes = models.IntegerField(default=0)
    wickets_taken = models.IntegerField(default=0)
    overs_bowled = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    runs_conceded = models.IntegerField(default=0)
    catches_taken = models.IntegerField(default=0)
    stumpings = models.IntegerField(default=0)
    man_of_the_match = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('match', 'player') # Ensure one entry per player per match

    def __str__(self):
        return f"{self.player.name} - {self.match}"