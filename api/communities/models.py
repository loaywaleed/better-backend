from django.db import models

class Community(models.Model):
    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name