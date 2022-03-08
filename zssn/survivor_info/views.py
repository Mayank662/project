from django.shortcuts import render
from . forms import survivor
# Create your views here.

def survivor_fun(request):
    if request.method == 'GET':
        form_obj = survivor()
        return render(request,'survivor_form.html',{'form':form_obj})
    
