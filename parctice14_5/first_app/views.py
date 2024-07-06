from django.shortcuts import render,redirect
from .forms import contactForm,StudentForm
# Create your views here.
def home(request):
    if request.method=='POST':
        form=contactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("basepage")
    else:
        form=contactForm()
    return render(request,'./first_app/django_form.html',{'form':form})
def model(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("basepage")
    else:
        form=StudentForm()
    return render(request,'./first_app/django_form.html',{'form':form})
    
