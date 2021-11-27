from django.shortcuts import render, redirect

# Create your views here.
from account.forms import RegisterForm


def index(request):
    return render(request, 'account/index.html', {})


def login(request):
    return render(request, 'account/login.html', {})


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            return redirect('validation')
    return render(request, 'account/register.html', {'form': form})


def validation(request):
    return render(request, 'account/validation.html', {})
