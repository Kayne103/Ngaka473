from django.urls import path

from account.views import user_list

urlpatterns = [
    path('', user_list)
]
