from django import forms
from . import models

class CreateEmployee(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ['username', 'password', 'email']