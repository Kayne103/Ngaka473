from django.shortcuts import render
from account.models import User


# Create your views here.
def index(request):
    return render(request, 'account/index.html', {})


def user_list(request: object) -> object:
    user = User.objects.all()
    context = {
        'user_list': user
    }
    return render(request, 'account/users.html', context)


def login(request):
    return render(request, 'account/login.html', {})


def register(request):
    return render(request, 'account/register.html', {})
