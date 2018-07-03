from django.shortcuts import render
from django.http import HttpResponse #Don't forget to include this. This is very important.

def index(request):
    
    #returning a page
    return render(request,'polls/index.html')

def test(request):

    return render(request,'polls/test.html')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s." % question_id
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)