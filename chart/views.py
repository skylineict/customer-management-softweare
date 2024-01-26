from django import views
from django.shortcuts import render
from django.views.generic import ListView, View

# Create your views here.

class StudentChart(View):
    def get(self, request):
        return render(request, 'chart/index.html')
