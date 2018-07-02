from django.shortcuts import render
from django.http import HttpResponse #Don't forget to include this. This is very important.

def index(request):
    
    #returning a page
    return render(request,'polls/index.html')

def test(request):

    return render(request,'polls/test.html')