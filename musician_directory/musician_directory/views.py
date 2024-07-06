from django.shortcuts import render
from musician.models import Musician

def home(request):
    data = Musician.objects.prefetch_related('albums').all()
    return render(request, "home.html", {'data': data})
