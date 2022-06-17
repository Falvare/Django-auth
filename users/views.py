from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy

from .forms import RegistrationForm

# Create your views here.
def register(requests):
    if requests.method == 'POST':
        form = RegistrationForm(requests.POST)
        if form.is_valid():
            form.save()
            reverse_lazy('login')
        else:
            form = RegistrationForm()
    
    form = RegistrationForm()

    context = {"form":form}

    return render(requests, 'registration/register.html', context)

def success(requests):
    return render(requests, 'registration/success.html')