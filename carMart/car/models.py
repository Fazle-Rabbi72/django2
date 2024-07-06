from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User
# Create your models here.
class Car(models.Model):
    name=models.CharField(max_length=50)
    color=models.CharField(max_length=30,null=True,blank=True)
    description=models.CharField(max_length=500)
    price=models.IntegerField()
    quantity=models.IntegerField()
    image=models.ImageField(upload_to='car/media/uploads/',blank=True,null=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name
    
class Comment(models.Model):
    car=models.ForeignKey(Car,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=30)
    email=models.EmailField() 
    body=models.TextField()     
    created_on=models.DateTimeField(auto_now_add=True)#live time

    def __str__(self):
        return f'Commented by {self.name}'