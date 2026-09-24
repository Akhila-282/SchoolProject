from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def profiles(request):
    # return HttpResponse("<H1>profiles</H1>")
    return render (request,'profiles.html',{})