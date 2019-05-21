from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.timezone import datetime
from event_task.models import Day_task,Event
# Create your views here.

@login_required
def dash(request):
    today=datetime.today()
    print(today.day)
    tasks=Day_task.objects.filter(day=today.day,month=today.month,year=today.year)
    events=Event.objects.filter(date=today)
    return render(request,'dashboard/index.html',{'month':today.month,'year':today.year,'tasks_today':tasks,'events':events})
