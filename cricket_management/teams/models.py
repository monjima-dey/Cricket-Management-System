from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    coach = models.CharField(max_length=100, blank=True, null=True)
    captain = models.ForeignKey('players.Player', on_delete=models.SET_NULL, null=True, blank=True, related_name='captain_of')
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name