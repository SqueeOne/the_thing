from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/<int:c_year>/', views.work_month, name="work_month"),
    path('<int:user_id>/<int:c_year>/<int:c_month>/', views.work_month_single, name="work_month_single"),
    path('<int:user_id>/<int:c_year>/<int:c_month>/<int:c_day>/', views.work_day_single, name="work_day_single"),
    path('<int:user_id>/divide/<int:work_day_id>/', views.divide_work_day, name="divide_work_day"),
    ]
    
