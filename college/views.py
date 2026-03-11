from django.shortcuts import render
from django.http import HttpResponse

def collegeGreet(request):
    return HttpResponse("Hello College!")
