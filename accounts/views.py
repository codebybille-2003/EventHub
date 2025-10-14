# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Account created successfully! Please login.")
            return redirect('login')
        else:
            messages.error(request, "⚠️ Please correct the highlighted errors below.")
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"🎉 Welcome {user.username}!")
            return redirect('event_list')
        else:
            messages.error(request, "❌ Invalid username or password.")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "👋 Logged out successfully.")
    return redirect('login')
