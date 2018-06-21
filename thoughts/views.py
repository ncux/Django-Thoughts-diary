from django.shortcuts import render, redirect
from .models import Thought
from .forms import ThoughtForm


def thoughts(request):
    thoughts_list = Thought.objects.order_by('-added_on')
    template = 'thoughts/thoughts.html'
    context = {"thoughts": thoughts_list}
    return render(request, template, context)



def enter(request):
    if request.method == 'POST':
        form = ThoughtForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/thoughts')

    else:
        form = ThoughtForm()

    template = 'thoughts/add.html'
    context = {'form': form}
    # print(request.POST.get('title'))
    # print(request.POST.get('content'))

    return render(request, template, context)