import builtins
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib import messages
from .models import Bulkemail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, send_mail
from customer.settings import EMAIL_HOST_USER
from .forms import myform

# Create your views here.


class EmailView(ListView):
    def get(self, request):
        Emailto = myform()
        context = {"emailto": Emailto}

        return render(request, 'email/index.html', context=context)

    def post(self, request):
        Emailto = myform(request.POST)
        context = {"emailto": Emailto}
        if Emailto.is_valid():
            Emailto = Emailto.cleaned_data['Emailto']
        # geting user data
        emailsubject = request.POST['emailsubject']
        reply = request.POST['reply']
        Fromemail = request.POST['Frommail']
        subject = request.POST['emailbody']
        # validating user
        if not emailsubject:
            messages.error(request, "Email Subject Empity")
            return render(request, 'email/index.html', context=context)
        Bulkemail.objects.create(EmailSubject=emailsubject, Replyto=reply,
                                 fromEmail=Fromemail, Emailto=Emailto, body=subject)

        html_message = render_to_string(
            template_name="email/email_comfirmation1.html")
        messagesneder = EmailMultiAlternatives(
            emailsubject, subject, EMAIL_HOST_USER, [
                Emailto]
        )
        messagesneder.attach_alternative(html_message, 'text/html')
        messagesneder.send()

        messages.success(request, "email send sucessfully ")
        return render(request, 'email/index.html', context=context)

        # creating user
        # messages.success(request, 'sucessfully created.. redrecting'
