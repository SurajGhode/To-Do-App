from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    reminder = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'autocomplete': 'off'}),
        input_formats=['%d-%m-%Y']
    )

    class Meta:
        model = Task
        fields = ['title', 'reminder']
