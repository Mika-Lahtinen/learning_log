from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """Home Page"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Get topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'larning_logs/topics.html', context)