from django.shortcuts import render
from .models import Topic
from django.http import HttpResponseRedirect
from django.core import reverse
from .forms import TopicForm

# Create your views here.
def index(request):
    """Home Page"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Get topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show the details of specified topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Add new topic"""
    if request.method != 'POST':
        # Not submmited : Create new table
        form = TopicForm()
    else:
        # Deal with submmited data
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

