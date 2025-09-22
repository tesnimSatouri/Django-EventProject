from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Hello(request,classe):
    return HttpResponse("Bonjour <i>"+classe+"</i>");