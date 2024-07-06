from django.db import models
from django.contrib.auth.models import User
from car.models import Car

# Create your models here.
class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='orders')
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING, related_name='cars')
    created_on = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.car.name} Bought By {self.buyer.username}"