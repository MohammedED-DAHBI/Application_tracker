from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("candidates:list")
    
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            return redirect("candidates:list")
    if request.user.is_authenticated:
        return redirect("candidates:list")
    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required(login_url="/")
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("users:login")
    
@login_required(login_url="/")
def profile(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            logout(request)
            return redirect('users:login')
        else:
            messages.error(request, 'please correct the error below')
    user = request.user
    return render(request, 'users/profile.html', {'username': user.get_username(), 'mail': user.email})