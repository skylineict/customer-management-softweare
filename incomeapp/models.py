from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class myincome(models.Model):
    incomeAmount = models.FloatField(max_length=200)
    incomeowner =  models.ForeignKey(User, on_delete=models.CASCADE)
    inconmedate  = models.DateField(auto_created=True)
    incometype   =  models.CharField(max_length=200)
    incomesource =   models.CharField(max_length=2000)



    def __str__(self):
        return self.incomeAmount
    
    class Meta:
        ordering = ['-inconmedate']

class Source(models.Model):
    source = models.CharField(max_length=200)

    def __str__(self):
        return  self.source


class Incomeplan(models.Model):
    incometype = models.CharField(max_length=200, verbose_name='incomeplans')

    def __str__(self):
        return  self.incometype


