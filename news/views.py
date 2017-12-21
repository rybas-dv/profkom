from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'prof/home.html')

def documents(request):
    news = Konkurs.objects.all()
    context = {
        'news': news
    }
    return render(request, 'prof/documents.html', context)

def base(request):
    return render(request, 'prof/base.html')

