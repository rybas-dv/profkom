from django.shortcuts import render
from .models import *

# Create your views here.

def smotrikonkurs(request):
    smotr = SmotrKonkurs.objects.filter(is_active=True)
    return render(request, 'prof/smotri-konkurs.html', locals())

