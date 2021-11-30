from django.urls import path

from dashboard.views import *

urlpatterns = [
    path('client', client_dashboard, name='client'),
    path('assistant', assistant_dashboard, name='assistant'),
    path('doctor', doctor_dashboard, name='doctor')
]
