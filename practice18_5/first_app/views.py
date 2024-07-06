from django.shortcuts import render,redirect
from .forms import RegistretionFrom,UserChangeData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.
def home(request):
    return render(request,('home.html'))

def signup(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=RegistretionFrom(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfuly')
                form.save()
                print(form.cleaned_data)
        else:
            form=RegistretionFrom()
        return render(request,'signup.html',{'form':form})
    else:
        return redirect('profile')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('username')
            userpass = form.cleaned_data.get('password')
            user = authenticate(username=name, password=userpass)  # Check if the user exists in the database
            if user is not None:
                login(request, user)
                messages.success(request, 'logged in  successfuly')
                return redirect("profile")  # Redirect to the homepage
        # If form is not valid, fall through to render the form again with errors
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
def user_logout(request):
    logout(request)
    return redirect('homepage')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'user':request.user})
    else:
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
    return render(request,'changepass.html',{'form':form}) 

def update_user(request):
    if  request.user.is_authenticated:
        if request.method=='POST':
            form=UserChangeData(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfuly')
                form.save()
                return redirect('update_user')
        else:
            form=UserChangeData(instance=request.user)
        return render(request,'./update.html',{'form':form})
    else:
        return redirect('update_user')


