from django.shortcuts import render
from news_sobytia.models import *

# Create your views here.
def home(request):
    return render(request, 'prof/home.html')

def base(request):
    return render(request, 'prof/base.html', locals())