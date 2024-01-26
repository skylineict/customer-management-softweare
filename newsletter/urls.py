from django.urls import path
from .views import MyEmailView, Commentmail, Myemailapp

urlpatterns = [
    path("", MyEmailView.as_view(), name="email"),
    path("sendemail", Commentmail.as_view(), name="me"),
    path('emaillist', Myemailapp.as_view(), name='li'),

]
