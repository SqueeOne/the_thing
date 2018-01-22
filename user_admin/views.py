from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

import datetime
import calendar
from calendar import monthrange
from time import strftime

from .forms import WorkDayForm
from .models import WorkDay

def index(request):
    
    return render(request, 'user_admin/index.html')


def work_month(request, user_id, c_year):
    current_year = datetime.date.today().year
    
    months = list(range(1, 13))
    months_named = []
    
    for month in months:
        months_named.append(calendar.month_name[month])
        
    return render(request, 'user_admin/work_month.html', {'months_named': months_named, 'current_year': current_year})
    

def work_month_single(request, user_id, c_year, c_month):
    days_in_month = monthrange(c_year, c_month)[1]
    days_list = list(range(1, days_in_month+1))
    days_list_dated = []
    
    for item in days_list:
        days_list_dated.append(datetime.date(c_year, c_month, item))
    
    user_work_time = {}    
    work_time = WorkDay.objects.filter(worker=user_id)
    
    for item in work_time:
        user_work_time[item.day] = (item.start_time, item.end_time)
        
    current_month = calendar.month_name[c_month]
    time_list = []
    calc = 0
    
    for item, value in user_work_time.items():
        if item.month == c_month:
            time_converted_start = value[0].hour*60 + value[0].minute
            time_converted_end = value[1].hour*60 + value[1].minute
            temp = (time_converted_end - time_converted_start)/60
            time_list.append(temp)
            calc+=temp
        
    return render(request, 'user_admin/work_month_single.html', {'days_list_dated': days_list_dated, 'user_work_time': user_work_time, 'c_year': c_year, 'c_month': c_month, 'current_month': current_month, 'calc': calc, 'time_list': time_list})
    
    
def work_day_single(request, user_id, c_year, c_month, c_day):
    try:
        wd_instance = get_object_or_404(WorkDay, worker=user_id, day=datetime.date(c_year, c_month, c_day))
        form = WorkDayForm(instance=wd_instance)
    except Exception as e:
        form = WorkDayForm(request.POST or None)
        
    if request.method == 'POST':
        try:
            wd_instance = get_object_or_404(WorkDay, worker=user_id, day=datetime.date(c_year, c_month, c_day))
            form = WorkDayForm(request.POST, instance=wd_instance)
        except Exception as e:
            form = WorkDayForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.worker = get_object_or_404(User, pk=user_id)
            instance.day = datetime.date(c_year, c_month, c_day)
            instance.save()
            return redirect('work_month_single', user_id, c_year, c_month)
        else:
            print(form.errors)
    
    return render(request, 'user_admin/work_day_single.html', {'form': form})
    
    
def divide_work_day(request, work_day_id):
    work_day = get_object_or_404(WorkDay, pk=work_day_id)
    hours_worked = ((work_day.end_time.hour*60 + work_day.end_time.minute) - (work_day.start_time.hour*60 + work_day.start_time.minute))/60
    
    return render(request, 'user_admin/divide_work_day.html', {'hours_worked': hours_worked})