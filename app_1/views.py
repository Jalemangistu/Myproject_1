from django.shortcuts import render

# Create your views here.
from django.http  import HttpResponse
from app_1 .models import training
from app_1 import views
def home(request):
    if request.method=='POST':
        t_name=request.POST['training_name']
        t_provider=request.POST['training_provider']
        t_description=request.POST['description']
        
        if len(t_name)< 3:
            return HttpResponse('please enter proper training name')
        else:
            training_list= training(training_name=t_name,training_provider=t_provider,description=t_description)
            training_list.save()
    return render(request, 'home.html', {})