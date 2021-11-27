from django.urls import path

from account.views import login, index, register, validation

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('validation', validation, name='validation'),
]
