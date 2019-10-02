from django.urls import path, include
# from . import views

app_name='users'

urlpatterns = [
    # Default
    path('', include('django.contrib.auth.urls')),

]
