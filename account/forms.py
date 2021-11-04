from django.contrib.auth.forms import UserCreationForm

from account.models import Patient


class RegisterForm(UserCreationForm):
    class Meta:
        model = Patient
        fields = ['firstname', 'lastname', 'email', 'password',
                  'confirmPassword', 'address', 'dateOfBirth', 'gender', 'cellNumber']
