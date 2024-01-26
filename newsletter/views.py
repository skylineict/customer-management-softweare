import builtins
from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, EmailMessage
from customer.settings import EMAIL_HOST_USER
from .models import EmailSubcription, Messages, Emailist, Emailcontact
from django_pandas.io import read_frame
from django.core.mail import send_mail
from django.template.loader import get_template


# Create your views here.


class MyEmailView(ListView):
    def get(self, request):
        return render(request, 'email/index1.html', )

    def post(self, request):
        email = request.POST['email']
        if not email:
            messages.error(request, "Email field cannot be empty")
            return render(request, 'email/index1.html',)
        EmailSubcription.objects.create(Email=email)
        messages.success(request, "Email Submitted sucessfuly")
        return render(request, 'email/index1.html',)


class Commentmail(ListView):
    emailread = Messages.objects.all()

    def get(self, request):
        return render(request, 'email/index2.html',)

    def post(self, request):
        emailread = EmailSubcription.objects.all()
        df = read_frame(emailread, fieldnames=['Email'])
        emaillist = df['Email'].values.tolist()
        print(emaillist)
        title = request.POST['title']

        if not title:
            messages.error(request, 'title can not be empty')
            return render(request, 'email/index2.html',)
        Messages.objects.create(Title=title,)

        messages.success(request, "Email Submitted sucessfuly")
        myhtmlmessage = render_to_string(
            template_name='email/email_comfirmation1.html')

        mail = EmailMessage(
            subject=title,
            body=myhtmlmessage,
            from_email=EMAIL_HOST_USER,
            to=emaillist,
            reply_to=['info@skylineict.com'],)
        mail.content_subtype = 'html'
        mail.send()
        return render(request, 'email/index2.html',)


class Myemailapp(ListView):

    def get(self, request):
        emaillist = Emailist.objects.all()
        contaxt = {
            'emaillist': emaillist

        }
        return render(request, 'email/emaillist.html', context=contaxt)

    def post(self, request):
        emaillist = Emailist.objects.all()
        contaxt = {
            'emaillist': emaillist}
        email = request.POST['email']
        maillist = request.POST['email']
        if not email:
            messages.error(request, 'email filed empty')
            return render(request, 'email/emaillist.html', context=contaxt)
        Emailcontact.objects.create(email=email, )
        messages.success(request, 'email list sumiited successfully')
        return render(request, 'email/emaillist.html', context=contaxt)
