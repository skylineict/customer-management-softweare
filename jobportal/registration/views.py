from django.shortcuts import render
from django.views.generic import ListView, View

# Create your views here.

class Registration(View):
    def get(self, request):
        return render(request, 'home/registration.html')

