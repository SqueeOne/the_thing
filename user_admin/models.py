from django.db import models
from django.contrib.auth.models import User

class WorkDay(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField(blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_sick_leave = models.BooleanField(default=False)
    is_vacation = models.BooleanField(default=False)
    
    def __str__(self):
        return self.worker.username + ' - ' + str(self.day)