from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse 
from django.template import loader
from django.urls import reverse
from .models import Choice, Question 

def index (request): 
    
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
   
    template = loader.get_template('polls/index.html')
    
    context = { 'latest_question_list': latest_question_list, }
    
    #output = ', '.join([q.question_text for q in latest_question_list])
    
    return render(request, 'polls/index.html', context) 


def details (request, question_id): 
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question} )


def results (request, question_id): 
    question = get_object_or_404(Question, pk=question.id)
    return render (request, 'polls/results.html', {'question': question})


def vote (request, question_id): 
    question = get_object_or_404(Question)
    try: 
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNOtExist): 
        return render (request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice.",})
    # returns an HttpResponseREdirect after succesful dealing with post data. THis prevents data from being posted twice if a user hits the back button. 
    else: 
        selected_choice.votes +=1 
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))
