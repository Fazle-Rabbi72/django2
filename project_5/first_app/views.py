from django.shortcuts import render
from .forms import contactForm,stForm,passwordvaliditionForm
# Create your views here.
def home(request):
    return render(request,'./first_app/home.html')
def about(request):
    if request.method=='POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        select=request.POST.get('select')
        return render(request,'./first_app/about.html',{'name':name, 'email':email, 'select':select})
    else:
         return render(request,'./first_app/about.html')
def form(request):
    return render(request,'./first_app/form.html')
def Djangoforms(request):
    if request.method=='POST':
        form=contactForm(request.POST,request.FILES)
        if form.is_valid():
            file=form.cleaned_data['file']
            with open('./first_app/upload/'+file.name,'wb+')as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request,'./first_app/django_form.html',{'form':form})
    else:
        form=contactForm()

    return render(request,'./first_app/django_form.html',{'form':form})


# validation form for validition
def StudentForm(request):
    if request.method=='POST':
        form=stForm(request.POST,request.FILES)
        if form.is_valid():

            return render(request,'./first_app/django_form.html',{'form':form})
    else:
        form=stForm()
    return render(request,'./first_app/django_form.html',{'form':form})

def passForm(request):
    if request.method=='POST':
        form=passwordvaliditionForm(request.POST,request.FILES)
        if form.is_valid():

            return render(request,'./first_app/django_form.html',{'form':form})
    else:
        form=passwordvaliditionForm()
    return render(request,'./first_app/django_form.html',{'form':form})