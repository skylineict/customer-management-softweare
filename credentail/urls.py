from ast import Add
from django.urls import path
from .views import Forgetpassword, Completepassword, Completepasswordverification,Datetesting


urlpatterns = [
   path('', Forgetpassword.as_view(), name='forgetpass'),
   path('Completepassword/<uid>/<token>',Completepassword.as_view(), name='completepassword'),
   path('passwordcompleted/', Completepasswordverification.as_view(), name= 'passwordcompleted'),
   path('mydate/', Datetesting.as_view(), name= 'dateme')




   

]
