from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

# Create your models here.


class Usersetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.currency
