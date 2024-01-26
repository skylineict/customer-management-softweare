from django.db import models

# Create your models here.


class Bulkemail(models.Model):
    EmailSubject = models.CharField(max_length=50)
    Replyto = models.EmailField(max_length=50)
    Emailto = models.EmailField(default='skyl@gmail.com')
    fromEmail = models.EmailField(max_length=70)
    body = models.TextField(max_length=300, default="testing body")

    def __str__(self):
        return self.EmailSubject
