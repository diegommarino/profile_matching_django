from django.db import models
from profile_matching.profiles.models.profile import Profile


class Topic(models.Model):
    name = models.CharField(max_length=12)
    profile = models.ManyToManyField(Profile)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
