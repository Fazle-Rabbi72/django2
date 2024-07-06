from django.urls import path
from . import views

urlpatterns = [
    path('create_order/<int:id>', views.buy_car, name='create_order')
]