from django.db import models


# Create your models here.

class EmailSubcription(models.Model):
    Email = models.EmailField(max_length=300)
    Date = models.DateField(auto_now=True)


class Messages(models.Model):
    Title = models.CharField(max_length=500)
    message = models.TextField(max_length=10000)


class Emailist(models.Model):
    contact = models.CharField(max_length=200)

    def __str__(self):
        return self.contact


class Emailcontact(models.Model):
    email = models.EmailField(max_length=200)
    listemail = models.CharField(max_length=200, default='test')

    def __str__(self):
        return self.email
