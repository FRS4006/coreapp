from django.db import models
# Create your models here.
# discusison topic textfield into file field? 
# camelcase
# "container class holding many to many relationship"

class Participant(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70)
    studyid = models.CharField(max_length=30)
    startdate = models.DateField()

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
    videourl = models.URLField(max_length=150)

    class Meta:
        ordering = ["title"]
    
    def __str__(self):
        return self.title


class WeeklyAssignment(models.Model):
    weeknumber = models.CharField(max_length=30)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    discussionTopic = models.ManyToManyField(DiscussionTopic)
    skillVideo = models.ManyToManyField(SkillVideo)

    class Meta:
        ordering = ["weeknumber"]

    def __str__(self):
        return self.weeknumber