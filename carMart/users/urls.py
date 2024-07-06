from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserSignupView.as_view() ,name='signup'),
    path('signin/', views.UserSigninView.as_view() ,name='signin'),
    path('signout/', views.UserSignoutView.as_view() ,name='signout'),
    path('profile/', views.UserProfileView.as_view() ,name='profile'),
    path('profile/update', views.update_profile,name='update_profile'),
    path('reset_password/', views.reset_password,name='reset_password'),
    path('password_reset/', views.password_reset,name='password_reset'),
]