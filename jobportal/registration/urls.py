from django.urls import path
from .views import Registration


urlpatterns = [
    path('', Registration.as_view(),name='register')
    
]
