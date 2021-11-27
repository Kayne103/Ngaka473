from django.contrib.auth.forms import UserCreationForm
from account.models import Client
from django import forms

GENDER_OPTIONS = ['male', 'female']


class RegisterForm(UserCreationForm):
    firstname = forms.CharField(max_length=30, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Firstname'}))
    lastname = forms.CharField(max_length=30, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lastname'}))
    email = forms.EmailField(max_length=30, required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    address = forms.CharField(max_length=30, required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}))
    dateOfBirth = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Date of Birth'}))
    # gender = forms.CharField(max_length=30, required=True)
    cellNumber = forms.CharField(max_length=30, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cell Number'}))
    password1 = forms.CharField(max_length=30, required=True,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Password'}
                                ))
    password2 = forms.CharField(max_length=30, required=True,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Confirm password'}
                                ))

    class Meta:
        model = Client
        fields = ['firstname', 'lastname', 'email',
                  'address',  'cellNumber', 'dateOfBirth',
                  'password1', 'password2']
        #  'gender',

    def save(self, commit=True):
        client = super((RegisterForm, self).save(commit=False))
        client.email = self.cleaned_data['email']
        if commit:
            client.save()
        return client
