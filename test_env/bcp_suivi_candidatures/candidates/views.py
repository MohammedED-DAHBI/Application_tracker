from django.shortcuts import render
from .models import Candidate
# from django.http import HttpResponse

def candidates_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidates/candidates_list.html', {'candidates': candidates})

def candidate_details(request, slug):
    candidate = Candidate.objects.get(slug=slug)
    return render(request, 'candidates/candidate_details.html', {'candidate': candidate})