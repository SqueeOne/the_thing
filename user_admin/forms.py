from django.forms import ModelForm, HiddenInput, TextInput, CheckboxInput
from user_admin.models import WorkDay


class WorkDayForm(ModelForm):
    class Meta:
        model = WorkDay
        exclude = ['worker', 'day']
        widgets = {
            'start_time': TextInput(attrs={'class': 'form-control form-control-lg'}),
            'end_time': TextInput(attrs={'class': 'form-control form-control-lg'}),
            'is_vacation': CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_sick_leave': CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    