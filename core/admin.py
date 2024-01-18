from django.contrib import admin
from .models import Participant, WeeklyAssignment, DiscussionTopic, SkillVideo
# Register your models here.

admin.site.register(Participant)
admin.site.register(WeeklyAssignment)
admin.site.register(DiscussionTopic)
admin.site.register(SkillVideo)