from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    pass

class Addexpenses(models.Model):
    amount = models.FloatField(max_)
    purpose = models.TextField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=200)
    request_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.category

    class Meta:
        ordering = ['-date']


class Catergory(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name_plural = 'Categories'
