from django.shortcuts import render,redirect
from .forms import RegisterForm,ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfuly')
                form.save()
                print(form.cleaned_data)
        else:
            form=RegisterForm()
        return render(request,'signup.html',{'form':form})
    else:
        return redirect('profile')
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                name=form.cleaned_data['username']
                userpass=form.cleaned_data['password']
                user=authenticate(username=name, password=userpass)#check korteci user database a ace ki na 
                if user is not None:
                    login(request,user)
                    return redirect("profile") #profile page a ridirect korbe
        else:
            form=AuthenticationForm()
        return render(request,'./login.html',{'form':form})
    else:
        return redirect('profile')
    
def profile(request):
    if request.user.is_authenticated:
        return render(request,'./profile.html',{'user':request.user})
    else:
        return redirect('user_login')

def user_logout(request):
    logout(request)
    return redirect('user_login')
def pass_change(request):
    if request.method=="POST":
        form=PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)#password change korbe
            return redirect("profile")  
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'./passchange.html',{'form':form})   
 
def pass_change2(request):
    if request.method=="POST":
        form=SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)#password change korbe
            return redirect("profile")
        
    else:
        form=SetPasswordForm(user=request.user)
    return render(request,'./passchange.html',{'form':form})    


def change_user_data(request):
    if  request.user.is_authenticated:
        if request.method=='POST':
            form=ChangeUserData(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfuly')
                form.save()
                return redirect('change_user_data')
        else:
            form=ChangeUserData(instance=request.user)
        return render(request,'./update.html',{'form':form})
    else:
        return redirect('change_user_data')