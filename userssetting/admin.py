from django.contrib import admin
from .models import Usersetting

# Register your models here.


@admin.register(Usersetting)
class Usersetting(admin.ModelAdmin):
    list_display = ['user', 'currency']
