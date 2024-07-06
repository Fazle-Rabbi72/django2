from django.urls import path,include
from . import views

urlpatterns = [
    path('car_details/<int:pk>/',views.DetailsCarView.as_view(),name='car_details'),
]