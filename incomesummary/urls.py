from django.urls import path
from .views import csvexport,excelexport, exportpdf

urlpatterns = [
    # path('', Incomesumarry.as_view(), name='incomesumarry' ),
    path('csvfiles', csvexport,  name='csvfiles'),
    path('excel', excelexport,  name='excelfiles'),
    path('expensivepsdf', exportpdf,  name='exportpdf')
    
    
]
