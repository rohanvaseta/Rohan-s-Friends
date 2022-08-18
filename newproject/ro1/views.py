from django.shortcuts import render, redirect
from .models import Friends
from .forms import FriendsForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

def home(request):
    friends = Friends.objects.all()
    context={
        "friends" : friends
    }
    return render(request,"ro1/home.html", context=context)

def addFriend(request):
    if request.method == 'POST':
        form = FriendsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = FriendsForm()    
    context = {
        'form' : form
    }
    return render(request, 'ro1/create.html', context=context)

def friendDetail(request, id):
    friend = Friends.objects.get(id=id)
    context = {
        'friends' : friend
    }
    return render(request,'ro1/detail.html', context=context)

def deleteFriend(request, id):
    friends = Friends.objects.get(id=id)
    friends.delete()
    return redirect('home')

def editFriend(request, id):
    student = Friends.objects.get(id=id)
    if request.method == "POST":
        form = FriendsForm(request.POST, instance=student )   
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = FriendsForm(instance=student)
    return render(request, 'ro1/create.html',{'form': form})



# def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'ro1/index.html', context)

class IndexView(generic.ListView):
    template_name = 'ro1/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

# def detail2(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'ro1/detail2.html', {'question': question})
class DetailView(generic.DetailView):
    model = Question
    template_name = 'ro1/detail2.html'

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'ro1/result.html', {'question': question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'ro1/result.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'ro1/detail2.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))


