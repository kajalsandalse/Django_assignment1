from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def cse(request):
    return HttpResponse("welcome on cse page")

def etc(request):
    return HttpResponse("welcome on etc page")

def mech(request):
    return HttpResponse("welcome on mech page")

def civil(request):
    return HttpResponse("welcome on civil page")

