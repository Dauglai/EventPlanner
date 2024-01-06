from authentication.models import User
from django.db import models


class Type_Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тип мероприятия')

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название мероприятия')
    max_count = models.PositiveIntegerField(default=10, verbose_name='Максимальное количество участников')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    addres = models.CharField(max_length=100, verbose_name='Адрес')
    description = models.TextField(verbose_name='Описание')
    type_event = models.ForeignKey(Type_Event, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)


    def __str__(self):
        return self.title
