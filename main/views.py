from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'prof/home.html')

def documents(request):
    return render(request, 'prof/documents.html')

def base(request):
    return render(request, 'prof/base.html')