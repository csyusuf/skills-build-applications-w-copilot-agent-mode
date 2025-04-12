from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    class Meta:
        abstract = False

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ArrayField(model_container=User)
    class Meta:
        abstract = False

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    duration = models.IntegerField()
    class Meta:
        abstract = False

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    class Meta:
        abstract = False

class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    class Meta:
        abstract = False
