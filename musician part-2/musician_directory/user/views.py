from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.views.generic import FormView,TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django import forms
# Create your views here.

class UserSignupView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('signin')
    def form_valid(self, form):
        form.save()
        messages.success(self.request,'Account Has been registered successfully!')
        return super().form_valid(form)
    def get_context_data(self, **kwargs) :
        context=super().get_context_data(**kwargs)
        context['type']='Register'
        return context


class UserSigninView(LoginView):
    template_name = 'register.html'
    def get_success_url(self):
        return reverse_lazy('homepage')    
    def form_valid(self, form):
        messages.success(self.request,'User has been logged in successfully!')
        return super().form_valid(form)
    def get_context_data(self, **kwargs) :
        context=super().get_context_data(**kwargs)
        context['type']='Login'
        return context


class UserSignoutView(LogoutView):
    next_page=reverse_lazy('homepage')
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'User has been logged out successfully!')
        return super().dispatch(request, *args, **kwargs)
    
    
def password_reset(request):
    if request.user.is_authenticated:
        form = PasswordChangeForm(user=request.user)
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password has been changed successfully!')
        return render(request, './password_change.html', {'form': form,'type':'Reset Password With Old Password'})
    else:
        return redirect('signin')

def reset_password(request):
    if request.user.is_authenticated:
        form = SetPasswordForm(user=request.user)
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password has been changed successfully!')
        return render(request, './password_change.html', {'form': form,'type':'Reset Password Without Old Password'})
    else:
        return redirect('signin')
        