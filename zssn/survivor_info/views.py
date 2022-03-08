from django.http import HttpResponse
from django.shortcuts import render, redirect
from . forms import survivorForm
from . models import survivorModel
# Create your views here.

#To perform insret and update operation in form
def survivor_fun(request, id=0):
    if request.method == 'GET':
        if id==0:
            form_obj = survivorForm()
        else:
            person = survivorModel.objects.get(pk=id)
            form_obj = survivorForm(instance = person)
        return render(request,'survivor_form.html',{'form':form_obj})
    else:
        if id==0:
            form_obj = survivorForm(request.POST)
        else:
            person = survivorModel.objects.get(pk=id)
            form_obj = survivorForm(request.POST, instance = person)
        if form_obj.is_valid():
            form_obj.save()            
        context = {'survivor_list':survivorModel.objects.all()}
        return render(request,'survivor_list.html',context)

#To get the perecntage of infected and non-infected person
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