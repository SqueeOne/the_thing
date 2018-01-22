from django.db import models
from django.contrib.auth.models import User

class WorkDay(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_sick_leave = models.BooleanField(blank=True,default=False)
    is_vacation = models.BooleanField(blank=True, default=False)
    
    def __str__(self):
        return self.worker.username + ' - ' + str(self.day)
        
        
class Projects(models.Model):
    TYPE_CHOICES = (
        ('S', 'Slovenski'),
        ('M', 'Mednarodni'),
    )
    title = models.CharField(max_length=255)
    project_type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    project_budget = models.DecimalField(max_digits=7, decimal_places=2)
    project_ends = models.DateField()
    
    def __str__(self):
        return self.title