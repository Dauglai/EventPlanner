from django.contrib.auth.models import User
from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    deadline = models.DateTimeField()
    status = models.ForeignKey(Status, on_delete= models.CASCADE, null=True)

    def __str__(self):
        return self.title
