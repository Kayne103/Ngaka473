from django.shortcuts import render


#
# Create your views here.
def client_dashboard(request):
    return render(request, 'dashboard/client_dashboard.html')


def doctor_dashboard(request):
    return render(request, 'dashboard/doctor_dashboard.html')


def assistant_dashboard(request):
    return render(request, 'dashboard/assistant_dashboard.html')
