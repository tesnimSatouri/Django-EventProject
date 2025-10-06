from django.shortcuts import render
from .models import Event
# Create your views here.
def listEvent(request):
    list=Event.objects.all()
    return render(request,'Event/list.html',{'ll':list})