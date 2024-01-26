from urllib.parse import urlparse
from django.urls import path
from .views import StudentChart



urlpatterns = [

    path('', StudentChart.as_view(), name='chart')

    
]





