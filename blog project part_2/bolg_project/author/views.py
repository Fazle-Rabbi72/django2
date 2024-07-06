from django.shortcuts import render,redirect
from .forms import RegistrationForm,ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from posts.models import Post
# Create your views here.
# def add_author(request):
#     if request.method=='POST':
#         author_form=forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect("add_author")
#     else:
#         author_form=forms.AuthorForm() 
#     return render(request,"add_author.html",{'form':author_form})

def Registar(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfuly')
            form.save()
            print(form.cleaned_data)     
    else:
        form=RegistrationForm()
    return render(request,'registar.html',{'form':form ,'type':'Registar'})

def user_login(request):
   
    if request.method=='POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            name=form.cleaned_data['username']
            userpass=form.cleaned_data['password']
            user=authenticate(username=name, password=userpass)#check korteci user database a ace ki na 
            if user is not None:
                messages.success(request, 'Logged in successfuly')
                login(request,user)
                return redirect("profile") #profile page a ridirect korbe
            else:
                messages.warning(request, 'Login information incorrect')
                return redirect('Register')
    else:
        form=AuthenticationForm()
    return render(request,'./registar.html',{'form':form,'type':'Login'})

@login_required
def profile(request):
    data=Post.objects.filter(author=request.user)
    return render(request,'profile.html',{'data':data})
@login_required
def edit_profile(request):
    if request.method=='POST':
        profile_form=ChangeUserData(request.POST,instance=request.user)
        if profile_form.is_valid():
            messages.success(request, 'Profile updated successfuly')
            profile_form.save()
            return redirect("edit_profile")     
    else:
        profile_form=ChangeUserData(instance=request.user)
    return render(request,'update_profile.html',{'form':profile_form})

def user_logout(request):
    logout(request)
    return redirect('homepage')

def pass_change(request):
    if request.method=="POST":
        form=PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)#password change korbe
            return redirect("profile")
        
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'./passChange.html',{'form':form})   
 