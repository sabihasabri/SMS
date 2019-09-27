from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect 
from django.template import loader
from django.views import generic 
from django.urls import reverse
from .models import Choice, Question 

class IndexView (generic.ListView): 
    template_name = 'polling/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self): 
        return Question.objects.order_by('-pub_date')[:5]
    
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
   # template = loader.get_template('polling/index.html')
    
    #context = { 'latest_question_list': latest_question_list, }
    
    #output = ', '.join([q.question_text for q in latest_question_list])
    
    #return render(request, 'polling/index.html', context) 


class DetailView (generic.DetailView): 
    model = Question
    template_name = 'polling/detail.html'
    #question = get_object_or_404(Question, pk=question_id)
    #return render(request, 'polling/detail.html', {'question':question} )

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polling/result.html'
#def results (request, question_id): 
    #question = get_object_or_404(Question, pk=question_id)
    #return render (request, 'polling/result.html', {'question': question})


def vote (request, question_id): 
    question = get_object_or_404(Question, pk=question_id)
    try: 
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist): 
        return render (request, 'polling/detail.html', {'question': question, 'error_message': "You didn't select a choice.",})
    # returns an HttpResponseREdirect after succesful dealing with post data. THis prevents data from being posted twice if a user hits the back button. 
    else: 
        selected_choice.votes +=1 
        selected_choice.save()
        return HttpResponseRedirect(reverse('polling:results', args = (question.id,)))
