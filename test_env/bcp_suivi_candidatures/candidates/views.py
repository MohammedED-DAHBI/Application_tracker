from django.shortcuts import render, redirect
from .models import Candidate
from django.contrib.auth.decorators import login_required
from . import forms
from users.models import Employee
from django.core.serializers import serialize
from django.http import JsonResponse

@login_required(login_url="/")
def candidates_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidates/candidates_list.html', {'candidates': candidates})

@login_required(login_url="/")
def candidates_json(request):
    candidates = Candidate.objects.all()
    data = serialize('json', candidates)
    return JsonResponse(data, safe=False)

@login_required(login_url="/")
def candidate_details(request, id):
    candidate = Candidate.objects.get(id=id)
    if request.method == "POST":
        form = forms.CreateCandidate(request.POST, request.FILES, instance=Candidate.objects.get(id=id))
        if form.is_valid():
            form.save();
            return redirect('candidates:list')

    form = forms.CreateCandidate(instance=candidate)
    return render(request, 'candidates/candidate_details.html', {'candidate': candidate, 'form': form })

@login_required(login_url="/")
def new_candidate(request):
    if request.method == "POST":
        form = forms.CreateCandidate(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            newcandidate = form.save(commit=False)
            newcandidate.author = Employee.objects.get(user=request.user)
            newcandidate.save()
            return redirect('candidates:list')
    form = forms.CreateCandidate()
    return render(request, 'candidates/new_candidate.html', {'form': form})