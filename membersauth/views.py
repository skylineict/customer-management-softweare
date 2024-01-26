from email.mime import text
from django.contrib.auth import tokens
from django.db import models
from django.http import response
from django.shortcuts import redirect, render
from django.views.generic import CreateView, UpdateView, TemplateView, ListView, View
from dashapp.models import Post
from django.contrib.auth.models import User
import json
from .token import activateaccount
from validate_email import validate_email
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, send_mail
from customer.settings import EMAIL_HOST_USER
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib import auth


# Create your views here.
emailvildate = ['@gmail', '@', '.com']

# username ajax validation view


class Usernamenamevelidation(View):
    def post(self, request):
        # getting the body of the form and load it as json
        data = json.loads(request.body)
        username = data['username']  # getting the value of html
        if not str(username).isalnum():  # checking if the username contain a  charater and number
            return response.JsonResponse({'username_error':  'username should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return response.JsonResponse({'username_error': 'sorry username in use,choose another one'}, status=409)
        return response.JsonResponse({"username_valid": True})


class Emailvelidation(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return response.JsonResponse({'email_error': 'email entered not valid'}, status=400)
        if User.objects.filter(email=email).exists():
            return response.JsonResponse({'email_error': 'email already taken'})
        return response.JsonResponse({'email_valid': True})


class Registrationsview(View):
    def get(self, request):
        return render(request, "authapp/signup.html")

    def post(self, request):
        # geting user data
        # validating user
        # creating user
        # messages.success(request, 'sucessfully created.. redrecting')
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        password = request.POST['password1']
        comfirm_password = request.POST['password2']
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'password too short')
                    return render(request, "authapp/signup.html")
                user = User.objects.create_user(
                    username=username, email=email, first_name=first_name)
                user.set_password(password)
                user.is_active = False
                user.save()

                #
                # get current domain of the site
                current_site = get_current_site(request)
                subject = 'USER ACTIVATION ACCOUNT'
                text = 'below is your password'
                context = {
                    "user": user,
                    'sitedomain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.id)),
                    'token':  activateaccount.make_token(user)}
                html_message = render_to_string(
                    template_name='email/email_comfirmation.html', context=context)

                mymsg = EmailMultiAlternatives(
                    subject, text, EMAIL_HOST_USER, [email])
                mymsg.attach_alternative(html_message, 'text/html')
                mymsg.send()
                messages.success(
                    request, 'account created sucessfully, check email for activation')
                return render(request, "authapp/signup.html")

        return render(request, "authapp/signup.html")

# creating account activation for the email


class AccountActivation(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(
                uidb64))  # decoding the userid
            user = User.objects.get(pk=uid)
        except Exception:
            user = None
        if user is not None and activateaccount.check_token(user, token):
            user.is_active = True
            user.save()
            messages.info(request, "the account is activated sucesfully")
            return render(request, "authapp/email.html")
        else:
            messages.error(request, "invalid link may expired")
            return render(request, "authapp/email.html")


class UserLogin (View):
    def get(self, request):
        return render(request, "authapp/login.html")

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password1']
        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, "welcome" ' ' +
                                     username + '  ' "account sucessfully login ")
                    return redirect("dashboard")

                else:
                    messages.error(
                        request, "login faild, login to your email to activate your account")
                return render(request, "authapp/login.html")

            messages.error(request, "invalid login Password or Username")
            return render(request, "authapp/login.html")

        messages.error(request, "filled all filed")
        return render(request, "authapp/login.html")
