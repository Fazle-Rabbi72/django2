from django.shortcuts import render
from car.models import Car
from brand.models import Brand
from django.http import Http404 
def home(request,brand_slug=None):
    data=Car.objects.all()
    brands=None
    if brand_slug is not None:
        try:
            brands = Brand.objects.get(slug=brand_slug)
            data = Car.objects.filter(brand=brands)
          
        except Brand.DoesNotExist:

            raise Http404("Brand does not exist")
    brands=Brand.objects.all()
    return render(request,'home.html',{'cars':data,'brands':brands})