from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
   return render(request,'first_app/about.html')
def contact(request):
   return render(request,'first_app/contact.html')