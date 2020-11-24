from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'synerd/index.html')

def registration(request):
    return render(request, 'synerd/registration.html')