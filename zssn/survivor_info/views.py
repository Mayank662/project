from django.http import HttpResponse
from django.shortcuts import render, redirect
from . forms import survivorForm
from . models import survivorModel
# Create your views here.
'''
def survivor_list(request):
    context = {'survivor_list':survivorModel.objects.all()}
    return render(request, "survivor_list.html",context)
'''
def survivor_fun(request, id=0):
    if request.method == 'GET':
        if id==0:
            print('123')
            form_obj = survivorForm()
        else:
            person = survivorModel.objects.get(pk=id)
            form_obj = survivorForm(instance = person)
            print('Hello')
        return render(request,'survivor_form.html',{'form':form_obj})
    else:
        if id==0:
            print('kok')
            form_obj = survivorForm(request.POST)
        else:
            print('78965')
            person = survivorModel.objects.get(pk=id)
            form_obj = survivorForm(request.POST, instance = person)
        if form_obj.is_valid():
            form_obj.save()            
        context = {'survivor_list':survivorModel.objects.all()}
        return render(request,'survivor_list.html',context)
        
def report(request):
    infect_count = 0
    non_infect_count = 0
    survivor_data = list(survivorModel.objects.all())
    total_person = len(survivor_data)
    for i in range(total_person):
        if(survivor_data[i].infected):
            infect_count = infect_count+1
        else:
            non_infect_count = non_infect_count+1
    infect_per = (infect_count/total_person)*100
    non_infect_per = (non_infect_count/total_person)*100   
    return render(request,'result.html',{'infect_per':infect_per,'non_infect_per':non_infect_per})