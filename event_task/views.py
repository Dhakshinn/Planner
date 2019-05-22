from django.shortcuts import render,redirect
from .models import Event,Remember,Document,Task,Day_task
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.timezone import datetime
from .forms import Day_task_Form

# Create your views here.
@login_required
def events(request):
    events=Event.objects.all()
    return render(request,'event_task/event.html',{'events':events})

@login_required
def remember(request):
    remember=Remember.objects.all()
    return render(request,'event_task/remember.html',{'remember':remember})

@login_required
def task(request,month,year):
    month_code=["Nothing","January","Febrary","March","April","May","June","July","August","September","October","November","December"]
    all_tasks=Day_task.objects.all()
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        days=31
    else:
        days=30
    month_string=month_code[int(month)]
    month=int(month)
    prev_month=month-1
    next_month=month+1
    return render(request,'event_task/task.html',{'range':range(1,days),'year':year,'month':month,'prev_month':prev_month,'next_month':next_month,'month_string':month_string,'all_tasks':all_tasks})

def add_task(request,date_code,month_code,year_code):
    if request.method=='GET':
        form=Day_task_Form()
    else:
        form=Day_task_Form(request.POST)
        form.instance.day=date_code
        form.instance.month=month_code
        form.instance.year=year_code
        form.save()
        return redirect('dash')
    return render(request,'event_task/task_add.html',{'form':form})

class new_task(CreateView):
    model=Task
    template_name='event_task/task_add.html'
    fields='__all__'
    success_url=reverse_lazy('dash')

class task_update(UpdateView):
    model=Day_task
    template_name='event_task/task_add.html'
    fields=['tasks']
    success_url=reverse_lazy('dash')

@login_required
def document(request):
    document=Document.objects.all()
    return render(request,'event_task/document.html',{'document':document})

class event_add(CreateView):
    model=Event
    template_name='event_task/event_add.html'
    fields='__all__'
    success_url=reverse_lazy('event')

class event_update(UpdateView):
    model=Event
    template_name='event_task/event_add.html'
    fields='__all__'
    success_url=reverse_lazy('event')

class event_delete(DeleteView):
    model=Event
    template_name='event_task/delete.html'
    fields='__all__'
    success_url=reverse_lazy('event')

class remember_add(CreateView):
    model=Remember
    template_name='event_task/remember_add.html'
    fields='__all__'
    success_url=reverse_lazy('remember')

class remember_update(UpdateView):
    model=Remember
    template_name='event_task/remember_add.html'
    fields='__all__'
    success_url=reverse_lazy('remember')

class remember_delete(DeleteView):
    model=Remember
    template_name='event_task/delete.html'
    fields='__all__'
    success_url=reverse_lazy('remember')


class document_add(CreateView):
    model=Document
    template_name='event_task/document_add.html'
    fields='__all__'
    success_url=reverse_lazy('document')

class document_update(UpdateView):
    model=Document
    template_name='event_task/document_add.html'
    fields='__all__'
    success_url=reverse_lazy('document')

class document_delete(DeleteView):
    model=Document
    template_name='event_task/delete.html'
    fields='__all__'
    success_url=reverse_lazy('document')