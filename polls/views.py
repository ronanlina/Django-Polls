from django.shortcuts import render, get_object_or_404 #for return not found messages
from django.http import HttpResponse, HttpResponseRedirect #Don't forget to include this. This is very important.
from django.template import loader #used for getting the html files to be displayed
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """returns the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # #getting the page
    # template = loader.get_template('polls/index.html')
    
    # #maps objects to be sent to the htmls to be displayed/used
    # context = {
    #     'latest_question_list' : latest_question_list,
    # }

    # #returning a page
    # return HttpResponse(template.render(context, request))
    # #return render(request,'polls/index.html', context) #alternate

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    # question = get_object_or_404(Question, pk=question_id) #checks if found, else throw 404
    # return render(request, 'polls/detail.html', {'question' : question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) #gets the value from radiobutton named 'choice'
    except(KeyError, Choice.DoesNotExist):
        #redisplays question when no choice made
        return render(request,'polls/detail.html',{
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

def test(request):

    return render(request,'polls/test.html')