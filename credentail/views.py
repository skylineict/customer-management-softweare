import email
from multiprocessing import context
import datetime

from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
import pdb
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, send_mail
from django.db.models.query_utils import Q
from customer.settings import EMAIL_HOST_USER
from django.contrib import messages
import threading
# Create your views here.



    
#bulding a function that makes the email run faster 
class Emailsendingthread(threading.Thread):
    def __init__(self,myemaill):
        self.myemail= myemaill
        threading.Thread.__init__(self)
    
    #runing the task
    def run(self):
        self.myemail.send()
    
        
class Forgetpassword(View):
    def get(self, request):
        return render(request, 'authapp/emailverification.html')
    
    def post(self, request):
        emaildata = request.POST['email']
        myuser = User.objects.filter(Q(email=emaildata))

        currentdmain = get_current_site(request)
        subject =     'PASSWORD RESET REQUEST'
        body =        'hello your password reset is'

            
        if myuser.exists():
            # for myuser in myuser:
            context = {

                "username":myuser[0],
                'sitedomain': currentdmain.domain,
                'uid':       urlsafe_base64_encode(force_bytes(myuser[0].pk)),
                 'token':    PasswordResetTokenGenerator().make_token(myuser[0])

            }

            html_message =  render_to_string(template_name='authapp/emailverification2.html', context=context)
            myemaill = EmailMultiAlternatives(subject,body,EMAIL_HOST_USER, [emaildata] )
            myemaill.attach_alternative(html_message, 'text/html')
            Emailsendingthread(myemaill).start()
            messages.success(request, 'email reset token has been sent to  your email')
            return render(request, 'authapp/emailverification.html')

        messages.error(request, 'sorry email not found')
        return render(request, 'authapp/emailverification.html')


class Completepassword(View):
    def get(self,request,uid,token):
        user_id = urlsafe_base64_decode(force_str(uid))
        user = User.objects.get(pk=user_id)
        if not PasswordResetTokenGenerator().check_token(user,token):
            messages.error(request, 'Password reset link is invalid, kindly request a new one ')
            return redirect('forgetpass')
        else:
            return render(request, 'authapp/completpassword.html' )



    def post(self,request,uid,token):
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password!= password2:
            messages.error(request, 'Password  not the same try again ')
            return render(request, 'authapp/completpassword.html' )
        if len(password) < 6:
            messages.error(request, 'password is too shot, make use of 6 charaters')
            return render(request, 'authapp/completpassword.html' )
        

      
        user_id = urlsafe_base64_decode(force_str(uid))
        user = User.objects.get(pk=user_id)
        user.set_password(password)
        user.save()
        # messages.success(request, 'password has been change successfully,login with your new password')
        return redirect('passwordcompleted')

        # return render(request, 'authapp/completpassword.html' )


class Completepasswordverification(View):
    def get(self, request):

       return render(request,'authapp/emailverification3.html')


    def post(self, request):
        return render(request,'authapp/emailverification3.html')




class Datetesting(View):
    def get(self, request):
        todatsdate = datetime.date.today()

        tomorrow = todatsdate +  datetime.timedelta(days=1)
        sex_month_ago = todatsdate - datetime.timedelta(days=30*6)
        three_months = todatsdate + datetime.timedelta(days=30*3)
        hoursnow = todatsdate + datetime.timedelta(days=7)
        investment = 100000


        if tomorrow > three_months:
            profit = investment*5/100
        else:
            qualifyy = 'you have not qualify'
            



        context = {
            'todaydate':todatsdate,
            'tomorrow': tomorrow,
            'sex_month_ago':sex_month_ago,
             "three_months": three_months,
             'hoursnow'   : hoursnow,
              ' profit ':   profit 
              

             
        }
        return render(request,'authapp/newdatetime.html',context)


    def post(self, request):
        return render(request,'authapp/newdatetime.html')



        


