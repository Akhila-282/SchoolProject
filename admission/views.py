from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'index.html',{})


def products(request):
    return render(request,'products.html',{})

def services(request):
    # return HttpResponse("<h1>Services Available</h1>")
    return render(request,'services.html',{})

def login(request):
    return render(request,'login.html',{})