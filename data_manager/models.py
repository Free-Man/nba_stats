from django.db import models

class Team(models.Model):
  name = models.CharField(max_length=200)


class Game(models.Model):
  date = models.DateTimeField('date played')
  score_home = models.IntegerField(default=-1)
  score_away = models.IntegerField(default=-1)
  home_team = models.ForeignKey(Team)
  away_team = models.ForeignKey(Team)
  

class RatingSource(models.Model):
  name = models.CharField(max_length=200)
  website = models.CharField(max_length=200)
  
  
class PopularityRating(models.Model):
  team = models.ForeignKey(Team)
  rating = models.IntegerField(default=-1)
  source = models.ForeignKey(RatingSource)
  date_of_rating = models.DateTimeField("date of popularity")