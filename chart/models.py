from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.


class Student(models.Model):
    First_name = models.CharField(max_length=200)
    course    =  models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    email = models.CharField(max_length=200)



    def __str__(self):
        return self.email