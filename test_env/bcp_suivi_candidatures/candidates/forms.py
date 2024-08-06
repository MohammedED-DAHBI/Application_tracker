from django import forms
from . import models

class CreateCandidate(forms.ModelForm):
    class Meta:
        model = models.Candidate
        fields = ['name', 'status', 'cv']