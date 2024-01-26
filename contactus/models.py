from django.db import models

# Create your models here.


class Register(models.Model):

    email = models.CharField(max_length=40)
    uplaod_img = models.ImageField(upload_to="image")
    username = models.CharField(max_length=30)
    full_name = models.CharField(max_length=30)
    joindate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
