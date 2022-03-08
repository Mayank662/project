from django.http import HttpResponse
from django.shortcuts import render
from . forms import survivor
from . models import survivor_model
# Create your views here.

def survivor_fun(request):
    if request.method == 'GET':
        form_obj = survivor()
        return render(request,'survivor_form.html',{'form':form_obj})
    else:
        form = survivor(request.POST)
        if(form.is_valid()):
            form.save()            
            return render(request,'survivor_form.html',{'form':form})