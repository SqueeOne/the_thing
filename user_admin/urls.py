from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/<int:c_year>/', views.work_month, name="work_month"),
    path('<int:user_id>/<int:c_year>/<int:c_month>/', views.work_month_single, name="work_month_single"),
    ]
    
