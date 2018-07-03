from django.shortcuts import render, get_object_or_404 #for return not found messages
from django.http import HttpResponse #Don't forget to include this. This is very important.
from django.template import loader #used for getting the html files to be displayed
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    #getting the page
    template = loader.get_template('polls/index.html')
    
    #maps objects to be sent to the htmls to be displayed/used
    context = {
        'latest_question_list' : latest_question_list,
    }

    #returning a page
    return HttpResponse(template.render(context, request))
    #return render(request,'polls/index.html', context) #alternate

def test(request):

    return render(request,'polls/test.html')

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #checks if found, else throw 404
    return render(request, 'polls/detail.html', {'question' : question})

def results(request, question_id):
    response = "You're looking at the results of question %s." % question_id
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)