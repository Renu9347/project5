from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Akhil(request):
    return HttpResponse('<marquee><h1>Akhil is the best finisher in the world</marquee></h1>')
