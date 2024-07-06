from django.urls import path
from .import views
urlpatterns = [
    path('signup/',views.signup ,name="signup"),
    path('login/',views.user_login ,name="user_login"),
    path('logout/',views.user_logout ,name="user_logout"),
    path('changePassword/',views.pass_change,name="pass_change"),
    path('changePassword2/',views.pass_change2,name="pass_change2"),
    path('update/',views.change_user_data,name="change_user_data"),
    path('',views.home, name="homepage"),
    path('profile/',views.profile ,name="profile"),
]