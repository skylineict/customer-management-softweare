from multiprocessing import context
import re
from django import views
from django.shortcuts import redirect, render
from .models import myincome, Source, Incomeplan
from django.views.generic import ListView, View,CreateView
from django.contrib import messages
import pdb
from django.core.paginator import Paginator
import json 
from django.http import response
# Create your views here. 


#select all from  Source
# print(incomeSource)

incomeSource =  Source.objects.all()
incometype = Incomeplan.objects.all()

# def home(request):
#     incomes = myincome.objects.filter(incomeowner=request.user)
#     pdb.set_trace()


class Searchincom(View):
    def post(self,request):
        seachincome = json.loads(request.body).get('searchTextincome')
        incomes = myincome.objects.filter(incomeAmount__istartswith=seachincome,incomeowner=request.user) | myincome.objects.filter(
            inconmedate__istartswith=seachincome,incomeowner=request.user) | myincome.objects.filter(
            incometype__icontains=seachincome,incomeowner=request.user) | myincome.objects.filter(
            incomesource__icontains=seachincome,incomeowner=request.user)
        datas = incomes.values()  #this will return all the value as list
        return response.JsonResponse(list(datas),safe=False)
         


    
    

class Incomepage(View):
    def get(self, request):
        incomes = myincome.objects.filter(incomeowner=request.user)
        #select from income where owners ==users
        paginator = Paginator(incomes, 30)
        page_number = request.GET.get('page')
        obj_page = paginator.get_page(page_number)


        context ={
            'incoming':  obj_page
        }
        return render(request, 'dashboard/incomeapp/index.html',context=context)





class Addincome(CreateView):
    def get(self,request):
        mycontext = {
            "myincomesource": incomeSource,
            'incometype': incometype}
    
        return render(request, 'dashboard/incomeapp/Addincome.html',mycontext)
    
    def post(self,request):
        Amount = request.POST['amount']
        incomtype =   request.POST['incometype']
        date  = request.POST['date']
        sourceincome  = request.POST['source']
        myincome.objects.create(incomeAmount= Amount, inconmedate=date,incometype=incomtype,
         incomesource= sourceincome,   incomeowner=request.user )
        messages.success(request, 'Income has been added sucessfully')
        return redirect('incomepage')
       
        


class Editincomeapp(View):
    def get(self, request,pk):
        updateincomes = myincome.objects.get(pk=pk)
        # pdb.set_trace()
        context = {
            'incomesource': incomeSource,
            'incometpye':   incometype,
            'updateincomes': updateincomes,}
        return render(request, 'dashboard/incomeapp/update.html',context=context)
    

    def post(self, request, pk):
        updateincomes = myincome.objects.get(pk=pk)
        Amount = request.POST['amount']
        incomtype =   request.POST['incometype']
        date  = request.POST['date']
        sourceincome  = request.POST['source']
        updateincomes.incomeAmount = Amount
        updateincomes.incometype = incomtype
        updateincomes.incomesource = sourceincome
        updateincomes.inconmedate =  date
        updateincomes.incomeowner = request.user
        updateincomes.save()
        messages.success(request, 'income updated sucessfully ')
        return redirect('incomepage')
       


        



def deleteincome(request, pk):
    incomeapp = myincome.objects.get(id=pk)
    incomeapp.delete()
    messages.error(request, 'income app deleted sucssfully')
    return redirect('incomepage')
    
       
