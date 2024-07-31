from django.shortcuts import render
from .models import Candidate
from django.contrib.auth.decorators import login_required
from . import forms
# from django.http import HttpResponse

def candidates_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidates/candidates_list.html', {'candidates': candidates})

def candidate_details(request, slug):
    candidate = Candidate.objects.get(slug=slug)
    return render(request, 'candidates/candidate_details.html', {'candidate': candidate})

@login_required(login_url="/users/login/")
def new_candidate(request):
    if request.method == "POST":
        form = forms.CreateCandidate(request.POST, request.FILES)
        if form.is_valid():
            newcandidate = form.save(commit=False)
            newcandidate.author = request.user
            newcandidate.save()
            return render(request, 'candidates:list')
    form = forms.CreateCandidate()
    return render(request, 'candidates/new_candidate.html', {'form': form})