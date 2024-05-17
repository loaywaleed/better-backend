from django.db import models
from django.contrib.auth.models import User

class Community(models.Model):
    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    members = models.ManyToManyField(User)

    def __str__(self) -> str:
        return self.name