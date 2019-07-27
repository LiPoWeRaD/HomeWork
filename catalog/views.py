from django.shortcuts import render
from .models import *

def index(request):
    studentcunt = students.objects.count()


    return render(request, 'index.html', context={'studentcount': studentcunt})

# Create your views here.
