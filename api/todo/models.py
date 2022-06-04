from django.db import models


class todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    completed = models.BooleanField(default=False)
