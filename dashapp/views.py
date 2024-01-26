from ast import Try
from collections import UserDict
from locale import currency
from multiprocessing import context
from ntpath import join
from stat import FILE_ATTRIBUTE_READONLY
from django.core import paginator
from django.shortcuts import redirect, render
from django.views.generic import ListView, View
from pandas import concat
from userssetting.models import Usersetting
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Addexpenses, Catergory
from django.contrib import messages
from django.core.paginator import Paginator
import json
from django.contrib.auth.models import User
from django.http import JsonResponse, response
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from userssetting.views import filename
import pdb
import datetime
from  incomeapp.models import myincome


#reading and writing json files

# worldcurrency = []
# # pdb.set_trace()
# #opening the json files 
# with open(filename, 'r') as currency:

#     #reading the json files 
#     myfile = json.load(currency)
#     # for value, name in myfile.items():
#     for keys ,value in myfile.items():
#         worldcurrency.append({'mykeys':keys, "values":value })
    
#         # pdb.set_trace()




       

    
   
    
   




class Searchexpens(View):
    def post(self, request):
        search_str = json.loads(request.body).get('searchText')
        myexpenses = Addexpenses.objects.filter(amount__istartswith=search_str, request_by=request.user) | Addexpenses.objects.filter(
            purpose__icontains=search_str, request_by=request.user) | Addexpenses.objects.filter(
            date__istartswith=search_str, request_by=request.user) | Addexpenses.objects.filter(
            category__icontains=search_str, request_by=request.user)
        # converting the values to a list
        datas = myexpenses.values()
        # sending it to a network
        # the allow the josn to password
        return response.JsonResponse(list(datas), safe=False)
    # what is not a  dicgtionary


class Dashboard(LoginRequiredMixin, ListView):
    login_url = 'login'

    def get(self, request):
        expenses = Addexpenses.objects.filter(request_by=request.user)
        paginator = Paginator(expenses, 20)
        page_number = request.GET.get('page')
        obj_page = paginator.get_page(page_number)
        
        try:
            usercurrency = Usersetting.objects.get(user=request.user).currency
        except ObjectDoesNotExist:
          return redirect('userstting')
        context = {
            'expenses': obj_page,
            'usercurrency':  usercurrency
        }

        return render(request, 'dashboard/index.html', context=context)
# usercurrency = Usersetting.objects.get(user=request.user).currency

categories = Catergory.objects.all()


class Addexpens(LoginRequiredMixin,View):
    login_url ='login'
    def get(self, request):
        context = {
            "category": categories,
            'value': request.POST
        }
        return render(request, 'dashboard/addexpenses.html', context=context)

    def post(self, request): 
        context = {
            "category": categories,
            'value': request.POST
        }
        if request.method == 'POST':
            amount = request.POST['amount']
            purpose = request.POST['purpose']
            category = request.POST['category']
            date = request.POST['date']
            if not amount:
                messages.error(request, "Amount is required")
                return render(request, 'dashboard/addexpenses.html', context=context)
            if not purpose:
                messages.error(request, "Description is required")
                return render(request, 'dashboard/addexpenses.html', context=context)
            Addexpenses.objects.create(amount=amount, purpose=purpose, category=category,
                                       date=date, request_by=request.user)
            messages.success(request, "Expenses create sucessfully")
            return redirect('dashboard')


category = Catergory.objects.all()
# print(category)

class EditExpenses(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = "redirect_to"

    def get(self, request, pk):
        # getting the id of all the expenses
        expenses = Addexpenses.objects.get(pk=pk)
        context = {"expenses": expenses,
                   "value": expenses,
                   "category": category
                   

                   }
        
        return render(request, 'dashboard/edit_expenses.html', context=context)

    def post(self, request, pk):
        category = Catergory.objects.all()
        # getting the id of all the expenses
        expenses = Addexpenses.objects.get(pk=pk)
        context = {"expenses": expenses,
                   "value": expenses,
                   "category": category

                   }
        if request.method == 'POST':
            amount = request.POST['amount']
            purpose = request.POST['purpose']
            category = request.POST['category']
            date = request.POST['date']
            if not amount:
                messages.error(request, 'account fill requred')
                return render(request, 'dashboard/edit_expenses.html', context=context)
            if not purpose:
                messages.error(request, 'description required')
                return render(request, 'dashboard/edit_expenses.html', context=context)
            if not date:
                messages.error(request, 'date required')
                return render(request, 'dashboard/edit_expenses.html', context=context)
            # this code update the expense to the new one
            expenses.amount = amount
            expenses.purpose = purpose
            expenses.category = category
            expenses.date = date
            expenses.request_by = request.user
            expenses.save()
            messages.success(request, "expenses updated sucessfully")
        return redirect('dashboard')

# creating a delete function for my expensive project


def Deleteexpense(request, pk):
    expenses = Addexpenses.objects.get(id=pk)
    expenses.delete()
    messages.error(request, 'Expenses delete sucessfully ')
    return redirect('dashboard')


#expensive  chart for my app

def Summary_expensive_ajax(request):
    expensrep = {}
    todays = datetime.date.today()
    twomonths = todays- datetime.timedelta(days=30*3)
    expenses = Addexpenses.objects.filter(request_by=request.user,date__gte=twomonths,date__lte=todays)

        

    #getting the list of all expensive categoreis and remevoing depulicate 
    def get_category(expense):
        return expense.category
    categories_list = list(set(map(get_category,expenses)))

  
    #geting all the list of  expenses and adding it base on they category 
    def get_expensive_category_amount(categor):
        amount = 0
        filter_expenses_category = expenses.filter(category=categor)
        for item in filter_expenses_category:
            amount += item.amount
        return amount
        
    # for x in expenses:
    # getting all the expensive category and the amount sum togatheer 
    for y in  categories_list:
        expensrep[y]=get_expensive_category_amount(y)
    return JsonResponse({'expenses_data': expensrep},safe=False)

        
        
           
     

      
                
            
           
           

           
        # context ={ "amount":expenses,
        # 'twomonths': twomonths,
        # 'todays':  get_expensive_amount.,
        # 'categories_list': categories_list
        

        # }
       

        # return render(request, 'dashboard/incomeapp/expensive_sommary.html',context)


class Summary_expensive(View):
    def get(self, request):
        # todays = datetime.date.today() #getting todays date 
        # twomonths = todays- datetime.timedelta(days=30*4) #getting date from 3 months ago 
        # expenses = Addexpenses.objects.filter(request_by=request.user,date__gte=twomonths, date__lte=todays)
        # # getting all the expenses from  3 months and today 
       

        # expensiverep = {}
        # #get list of all category in the datbase
        # def category_expensive(expen):
        #     return expen.category
        # category_list = list(set(map(category_expensive, expenses)))
        # # pdb.set_trace()
       


        # def get_expenses_category_amount(category):
        #     amount = 0
        #     filtter_category = expenses.filter(category=category)
        #     for amount_in_categoey  in filtter_category:
        #         amount += amount_in_categoey.amount
        #     return amount
        
        # amount_list = map(get_expenses_category_amount, expenses)
        # # pdb.set_trace()

      

        # for mylist in category_list:
        #     return mylist


        # contex = {
        #     'amount_list': amount_list,
        #     'mylist': mylist

        # }
    



  

        return render(request, 'dashboard/incomeapp/expensive_sommary.html')
    
    
    def post(self, request):
        return render(request, 'dashboard/incomeapp/expensive_sommary.html')
    



def incomesummary_ajax(request):
    incomerep = {}
    todays_date = datetime.date.today()
    one_week_ago = todays_date - datetime.timedelta(days=30)
    incomessumarry = myincome.objects.filter(inconmedate__gte=one_week_ago,incomeowner=request.user)

        

    
    
 #getting the list of all expensive categoreis and remevoing depulicate
    def get_incomesource(incomesource):
        return incomesource.incomesource
    income_category = list(set(map(get_incomesource,incomessumarry)))

    
    #geting all the list of  expenses and adding it base on they category 
    def get_income_amount(comeAmount):
        amount = 0
        income_amount_incourse = incomessumarry.filter(incomesource=comeAmount)
        for amountincome in income_amount_incourse:
            amount += amountincome.incomeAmount
        return amount
    for w in income_category:
        incomerep[w]= get_income_amount(w)
        
    return JsonResponse({'income_data':incomerep},safe=False)


class Incomesumarry(View):
    def get(self, request):

         incomerep = {}
         todays_date = datetime.date.today()
         one_week_ago = todays_date - datetime.timedelta(days=30)
         incomessumarry = myincome.objects.filter(inconmedate__gte=one_week_ago,incomeowner=request.user)
         def get_incomesource(incomesource):
            return incomesource.incomesource
         income_category = list(set(map(get_incomesource,incomessumarry)))
         
        #  def get_income_amount(Amount):
        #     amount = 0
        #     income_amount_incourse = incomessumarry.filter(incomeAmount=Amount)
        #     for amountincome in income_amount_incourse:
        #         amount += amountincome.incomeAmount
        #         return amount
        #  pdb.set_trace()
                
         return render(request, 'dashboard/incomeapp/income_summary.html')


    def post(self, request):
        return render(request, 'dashboard/incomeapp/income_summary.html')