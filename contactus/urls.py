from django.urls import path
from .views import contactus


urlpatterns = [
    path("", contactus, name="contactus"),

]
