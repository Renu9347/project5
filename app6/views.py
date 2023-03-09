from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def kohli(request):
    return HttpResponse('<marquee><h1>kohli best batsman in the world</marquee></h1>')
