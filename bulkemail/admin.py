from django.contrib import admin
from .models import Bulkemail

# Register your models here.


@admin.register(Bulkemail)
class Admin(admin.ModelAdmin):
    list_display = ('EmailSubject', "Replyto",
                    "EmailSubject", "fromEmail", "body")
