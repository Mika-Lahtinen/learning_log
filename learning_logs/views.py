from django.shortcuts import render

# Create your views here.
def index(request):
    """Home Page"""
    return render(request, 'learning_logs/index.html')