from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import RegistrationForm

# Create your views here.
def register(requests):
    if requests.method == 'POST':
        form = RegistrationForm(requests.POST)
        if form.is_valid():
            form.save()
            reverse_lazy('login')
        else:
            messages.error(requests, 'Please correct form and try again')
            form = RegistrationForm()
    
    form = RegistrationForm()

    context = {"form":form}

    return render(requests, 'registration/register.html', context)

def profile(requests):
    return render(requests, 'registration/profile.html')