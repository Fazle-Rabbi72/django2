from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.home,name='homepage'),
    path('about/',views.about,name='aboutpage'),
    path('form/',views.form,name='form'),
    path('django_form/',views.Djangoforms,name='django_form'),
    path('student_form/',views.StudentForm,name='student_form'),
    path('pass_form/',views.passForm,name='pass_form'),

]
