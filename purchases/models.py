from django.contrib.auth.models import User
from django.db import models


class TypePurchase(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='uploads/% Y/% m/% d/')
    description = models.CharField(max_length=10000)
    price = models.PositiveIntegerField()
    type = models.ForeignKey(TypePurchase, on_delete= models.CASCADE, null=True)