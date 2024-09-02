from django import forms
from . import models

class CreateCandidate(forms.ModelForm):
    class Meta:
        model = models.Candidate
        fields = ['entity', 'sub_entity', 'position', 'name', 'teams_interview', 'technical_interview', 'oto_interview', 'cv', 'status', 'comment']