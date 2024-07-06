
from django.urls import path
from .import views
urlpatterns = [
   path('signup/',views.Registar, name="Registar"),
   path('login/',views.user_login, name="login"),
   path('logout/',views.user_logout ,name="user_logout"),
   path('profile/',views.profile, name="profile"),
   path('profile/changePass/',views.pass_change, name="pass_change"),
   path('profile/edit_profile/',views.edit_profile, name="edit_profile"),
]
