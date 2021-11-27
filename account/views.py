from django.shortcuts import render, redirect
from account.forms import RegisterForm
from django.contrib import messages


def index(request):
    return render(request, 'account/index.html', {})


def login(request):
    return render(request, 'account/login.html', {})


def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            client = form.save()
            # client.set_password(client.password)
            # form.save(commit=False)
            messages.success(request, 'Account created for ' + client)
            return redirect('validation')
    return render(request, 'account/register.html', {'form': form})


def validation(request):
    return render(request, 'account/validation.html', {})
