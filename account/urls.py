from django.urls import path

from account.views import login, index, register

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('register', register, name='register')
]
