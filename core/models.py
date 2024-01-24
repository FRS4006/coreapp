from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# discusison topic textfield into file field? 
# camelcase
# "container class holding many to many relationship"

class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70)
    studyID = models.CharField(max_length=30)
    startDate = models.DateField()


    def __str__(self):
        return self.name


class DiscussionTopic(models.Model):
    title = models.CharField(max_length=30)
    summary = models.TextField()

    class Meta:
        ordering = ["title"]
    
    def __str__(self):
        return self.title


class SkillVideo(models.Model):
    title = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    videoURL = models.URLField(max_length=150)

    class Meta:
        ordering = ["title"]
    
    def __str__(self):
        return self.title


class WeeklyAssignment(models.Model):
    weekNumber = models.CharField(max_length=30)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    discussionTopic = models.ManyToManyField(DiscussionTopic)
    skillVideo = models.ManyToManyField(SkillVideo)

    class Meta:
        ordering = ["weekNumber"]

    def __str__(self):
        return self.weekNumber