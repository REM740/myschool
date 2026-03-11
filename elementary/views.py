from django.shortcuts import render
from django.http import HttpResponse

def elementaryGreet(request):
    return HttpResponse("Hello elementary!")
