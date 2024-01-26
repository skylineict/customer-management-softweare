from django.contrib import admin
from .models import EmailSubcription, Messages, Emailcontact, Emailist

# Register your models here.


@admin.register(Messages)
class Adminsite(admin.ModelAdmin):
    list_display = ('Title', 'message')


@admin.register(EmailSubcription)
class Adminsite(admin.ModelAdmin):
    list_display = ('Email', 'Date')


@admin.register(Emailist)
class EmailCon(admin.ModelAdmin):
    list_display = ('contact',)


@admin.register(Emailcontact)
class EmaiList(admin.ModelAdmin):
    list_display = ('email', 'listemail')
