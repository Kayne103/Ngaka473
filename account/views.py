from django.shortcuts import render
from account.models import User


# Create your views here.

def user_list(request: object) -> object:
    user = User.objects.all()
    context = {
        'user_list': user
    }
    return render(request, 'account/users.html', context)

