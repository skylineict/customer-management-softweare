from django.contrib import admin
from .models import Catergory, Addexpenses

# Register your models here.


@admin.register(Addexpenses, Catergory)
class AdminFeatures(admin.ModelAdmin):
    pass
