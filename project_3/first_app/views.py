from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d={'authore':'Kodu molla','age':15,'lst':['python','is','best'],'course':[
        {
            'id':1,
            'name':'python',
            'fee':5000
        },
        {
            'id':2,
            'name':'django',
            'fee':10000
        },
        {
            'id':3,
            'name':'C',
            'fee':1000
        }
    ],'birthday':datetime.datetime.now(),'val':''}



    return render(request,'home.html',d)