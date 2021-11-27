from django.contrib.auth.forms import UserCreationForm

from account.models import Client


class RegisterForm(UserCreationForm):
    class Meta:
        model = Client
        fields = ['firstname', 'lastname', 'email',
                  'address', 'dateOfBirth', 'gender', 'cellNumber',
                  'password1', 'password2']
