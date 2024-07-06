from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def course(request):
    return HttpResponse("This is first app/course page")
def about(request):
    return HttpResponse("This is first app /about page")
def home(request):
    return HttpResponse("This is first app /home page")