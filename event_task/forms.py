from django import forms
from .models import Day_task


class Day_task_Form(forms.ModelForm):
    class Meta:
        model=Day_task
        fields=['tasks']