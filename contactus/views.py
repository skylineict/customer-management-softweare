from django.shortcuts import render
from .form import Contactus
from django.contrib import messages


# Create your views here.


def contactus(request):
    if request.method == 'POST':
        form = Contactus(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            fulll_name = form.cleaned_data['full_name']
            form.save()
            # context = {
            #     "email": email,
            #     "username": username,
            #     "fullname":  fulll_name
            # }
            messages.success(request, "contact info sumitted sucessfully ")
            return render(request, 'contactus/index.html', )
        else:
            messages.error(request, 'field to registered try again ')
            return render(request, 'contactus/index.html', {"form": form})

    else:

        form = Contactus()
    return render(request, 'contactus/index.html', {"form": form})
