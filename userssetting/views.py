import os

from django.shortcuts import redirect, render, HttpResponse
from django.views.generic import View, ListView
from django.conf import settings
import pdb
import json
from django.contrib import messages


from .models import Usersetting


# Create your views here.

currency_data = []
namev = []
valuename = []
# accessing the the json files
filename = os.path.join(settings.BASE_DIR, 'currencies.json')
with open(filename, 'r') as data:

    # opening the json files and read it
    mydata = json.load(data)  # loading the json files
    for k, v in mydata.items():
        # lopping into the json values and keys and saved them in empty veriable k and v
        # appending the k and v variables in empty currency list
        currency_data.append({'name': k, "value": v})

        # pdb.set_trace()


class UserSetting(View):
    def get(self, request):
        exist = Usersetting.objects.filter(user=request.user).exists()
        if exist:
            userpreferences = Usersetting.objects.get(user=request.user)
            return render(request, 'dashboard/usersetting/index.html', {'currency': currency_data, "userpreferences": userpreferences})

        return render(request, 'dashboard/usersetting/index.html', {'currency': currency_data})

    def post(self, request):
        # accsssing the input html name of the currency
        currency = request.POST['currency']
        # to check if the user already have selected currency
        if Usersetting.objects.filter(user=request.user).exists():
            # to get the currency the login user has selected
            userpreferences = Usersetting.objects.get(user=request.user)
            # to add the currency value from the database
            userpreferences.currency = currency
            userpreferences.save()
            messages.success(request, 'changes saved sucessfully ')
            return render(request, 'dashboard/usersetting/index.html', {'currency': currency_data, 'userpreferences': userpreferences})

        else:
            userset = Usersetting.objects.create(
                user=request.user, currency=currency)  # this is to create the corrency input value on
            userset.save()
            messages.success(request, 'currency save sucessfully  ')
            return render(request, 'dashboard/usersetting/index.html', {'currency': currency_data})

#         # already existing table on the databas and ALSO check the currency login user.

#         # pdb.set_trace()


def SettingsView(request):
    currency_data = []
    filename = os.path.join(settings.BASE_DIR, 'currencies.json')
    with open(filename, 'r') as data:

        # opening the json files and read it
        mydata = json.load(data)  # loading the json files
        for k, v in mydata.items():

            # lopping into the json values and keys and saved them in empty veriable k and v
            # appending the k and v variables in empty currency list
            currency_data.append({'name': k, "value": v})

    # checking if the login users has selected currecy
    existed = Usersetting.objects.filter(user=request.user).exists()
    userscurrency = None
    if existed:
        userscurrency = Usersetting.objects.get(user=request.user)

    if request.method == "POST":
        currency = request.POST['currency']

        if existed:
            userscurrency.currency = currency
            userscurrency.save()
            messages.success(request, "currency change sucessfully")
        else:
            Usersetting.objects.create(user=request.user, currency=currency)
            messages.success(request, "currency change sucessfully")
            return render(request, 'dashboard/usersetting/index.html', {'currency': currency_data, 'userpreferences':  userscurrency})

    return render(request, 'dashboard/usersetting/index.html', {'currency': currency_data, 'userpreferences':  userscurrency})
