from django.db import models
from django.contrib.auth.models import User


class Community(models.Model):
    """
    Model representing communities in the app
    """
    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    members = models.ManyToManyField(User, related_name='communities')
    admin = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='admin_communities')

    def __str__(self) -> str:
        return self.name


class CommunityHabit(models.Model):
    """
    Model representing community habits
    """
    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    # Number of days to do the habit per week
    frequency = models.IntegerField(null=True)
    motivation = models.TextField(null=True)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="habits")
