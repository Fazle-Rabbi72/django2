from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect,get_object_or_404
from .models import Order
from car.models import Car
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def buy_car(request, id):
    if request.method == 'POST':
        car = get_object_or_404(Car, pk=id)
        if car.quantity > 0:
            Order.objects.create(buyer=request.user, car=car)
            car.quantity -= 1
            car.save()
            messages.success(request, f"{car.name} has been purchased successfully!")
            return redirect('car_details', pk=car.pk)
        else:
            messages.error(request, f"Sorry, {car.name} is out of stock.")
            return redirect('car_details', pk=car.pk)
    else:
        return redirect('home')