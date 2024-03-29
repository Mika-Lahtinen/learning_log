from django.urls import path

from . import views

app_name='learning_logs'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    #show topics
    path('topics/', views.topics, name='topics'),
    #show spcified topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Add new webpage
    path('new_topic/', views.new_topic, name='new_topic'),
    # New entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Edit existed entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
