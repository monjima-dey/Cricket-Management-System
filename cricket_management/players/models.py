from django.db import models
from teams.models import Team

class Player(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='players')
    role = models.CharField(max_length=50, choices=[
        ('batsman', 'Batsman'),
        ('bowler', 'Bowler'),
        ('all-rounder', 'All-Rounder'),
        ('wicket-keeper', 'Wicket-Keeper'),
    ], blank=True, null=True)
    jersey_number = models.IntegerField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='player_profiles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name