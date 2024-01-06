from authentication.models import User
from django.db import models

from event.models import Event


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    deadline = models.DateTimeField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(Event, verbose_name='Событие', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, verbose_name='Организация', on_delete=models.CASCADE, related_name='owner')
    users = models.ManyToManyField(User, related_name='users')

    def __str__(self):
        return self.title
