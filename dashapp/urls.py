from django.urls import path
from .views import Dashboard, Addexpens, EditExpenses, Deleteexpense, Summary_expensive,Summary_expensive_ajax,incomesummary_ajax,Incomesumarry


urlpatterns = [
    path("", Dashboard.as_view(), name="dashboard"),
    path('addexpenses', Addexpens.as_view(), name='addexpenses'),
    path('editexpenses/<int:pk>', EditExpenses.as_view(), name='editexpenses'),
    path('delete/<int:pk>', Deleteexpense, name="delete"),
    path('expensive_summary', Summary_expensive.as_view(), name='expensive_sum'),
    path('Summary_expensive_ajax',Summary_expensive_ajax, name='Summary_expensive_ajax'),
    path('incomesummary_ajax', incomesummary_ajax, name='iname' ),
    path('incomeexpensive/', Incomesumarry.as_view(), name='incomesumarry' ),
    



]
