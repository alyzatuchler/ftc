from django.contrib.postgres import fields
from django.db import models


class Team(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=128)
    school = models.CharField(max_length=128)


class Judge(models.Model):
    name = models.CharField(max_length=128)
    experienced = models.BooleanField()
    conflicts = fields.ArrayField(models.IntegerField(), null=True, blank=True)
    technical = models.BooleanField()
    nontechnical = models.BooleanField()


class JudgingRoom(models.Model):
    room_number = models.IntegerField()
    judges = models.ManyToManyField(Judge, related_name="judging_room", blank=True)
    teams = models.ManyToManyField(Team, related_name="judging_room", blank=True)


class Award(models.Model):
    name = models.CharField(max_length=128)
    judges = models.ManyToManyField(Judge, related_name="judging_panel", blank=True)
    callback_teams = models.ManyToManyField(
        Team, related_name="callback_teams", blank=True
    )
    nominated_teams = models.ManyToManyField(
        Team, related_name="nominated_teams", blank=True
    )


class AwardNomination(models.Model):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    award = models.ForeignKey(Award, on_delete=models.SET_NULL, null=True, blank=True)
    ranking = models.IntegerField()
    announcement = models.CharField(max_length=5000)
