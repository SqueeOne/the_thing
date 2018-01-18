from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

import datetime
import calendar
from calendar import monthrange

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
        
    current_month = calendar.month_name[c_month]
        
    return render(request, 'user_admin/work_month_single.html', {'days_list_dated': days_list_dated, 'c_year': c_year, 'c_month': c_month, 'current_month': current_month})