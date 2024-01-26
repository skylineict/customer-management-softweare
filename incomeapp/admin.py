from django.contrib import admin
from .models import Incomeplan, myincome, Source

# Register your models here.

@admin.register(Incomeplan, myincome,Source)
class MYincomeap(admin.ModelAdmin):
    pass