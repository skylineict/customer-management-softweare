from base64 import encode
from email import header
import encodings
import imp
from math import frexp
import string
from urllib import response
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from  incomeapp.models import myincome
import datetime
import pdb
import csv
import xlwt
from django.http import HttpResponse, JsonResponse
from dashapp.models  import Addexpenses
from django.template.loader  import render_to_string
from weasyprint import HTML
import tempfile


# Create your views here.


def csvexport(request):
    # This tells browsers that the document is a CSV file, instead of HTML file.
    resp = HttpResponse(content_type = 'Text/CSV')

    # this code contains CSV filename and downloads files with that name.
    resp['Content-Disposition']  = 'attachment; filename="somefilename.csv'
    # here write the respons in csv document with the expentsion
    write = csv.writer(resp)
    write.writerow(['Amount', 'Category', 'Description', 'Date'])
    expenses = Addexpenses.objects.filter(request_by=request.user)
    for expens in expenses:
        write.writerow([expens.amount, expens.category, expens.purpose, expens.date])

    return resp



def excelexport(request):
    xcelrees = HttpResponse(content_type = 'application/ms-excel')
    # this code contains CSV filename and downloads files with that name.

    xcelrees['Content-Disposition']  = 'attachment; filename="myexpense' + \
         str(datetime.datetime.now())+'.xls'  #his contains CSV filename and downloads files with that name.
    wb = xlwt.Workbook(encoding='utf-8') # Creating a Workbook of encoding utf-8
    ws = wb.add_sheet('expense xcelbook')#Creating a Sheet named “Users Data” and all the data will be written inside this sheet.


    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['amount','description', 'category','date']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num],font_style)
    font_style = xlwt.XFStyle()

    rows = Addexpenses.objects.filter(request_by=request.user).values_list('amount','purpose', 'category','date')
    for row in rows :
        row_num +=1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]),font_style)
    wb.save(xcelrees)

    return xcelrees
    



def exportpdf(request):
    pdfresponse= HttpResponse(content_type = 'application/pdf')
    # this code contains CSV filename and downloads files with that name.

    pdfresponse['Content-Disposition']  = ' inline; attachment; filename="myexpense' + \
         str(datetime.datetime.now())+'.pdf'  #this code will  will downlaoded 
    
    pdfresponse['content transfer encoding'] = 'binary'   #transfering binary to html template 
    expenses = Addexpenses.objects.filter(request_by=request.user)

    html_string = render_to_string('authapp\pdf.html',{ 'expensive':expenses, 'total':0})

    html = HTML(string=html_string) #convertting the  html to a pdf

    result = html.write_pdf() #writingf the  html string to normal

    ##writing this pdf in a temp files


    #this programm story the pdf temp on the browser and also preview it

    with tempfile.TemporaryFile(delete=True) as  output:
        output.write(result)
        output.flush()
        output.seek(0)
        pdfresponse.write(output.read())
    return pdfresponse


def exportpdfs(request):
    return render(request, 'authapp\pdf.html')


    
 

        




 




    



    



    



    
# class Incomesumarry(View):
#     def get(self, request):
       
#         # pdb.set_trace()
       
#         # pdb.set_trace()
#         #getting the list of all expensive categoreis and remevoing depulicate 
#         # def get_incomesource(myincome):
#         #     return myincome.incomesource
#         # income_list = map(get_incomesource, incomessumarry)
        

#         # pdb.set_trace()

#         # context = {
#         #     'income': income_list,
#         #      'i': i

#         # }


#         return render(request, 'dashboard/incomeapp/income_summary.html')


#     def post(self, request):
#         return render(request, 'dashboard/incomeapp/income_summary.html')