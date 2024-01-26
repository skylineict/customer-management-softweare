from ast import Add
from django.urls import path
from .views import Incomepage, Addincome,deleteincome,Editincomeapp, Searchincom
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path('income', Incomepage.as_view(), name='incomepage'),

    path('addincome/', Addincome.as_view(), name='addincome'),

    path('updateincome/<int:pk>',Editincomeapp.as_view(), name='updateincome' ),
    
    path('mydelete/<int:pk>',deleteincome, name='mydelete' ),
    path('income-searching', csrf_exempt(Searchincom.as_view()), name='income')


   

]
