from django.shortcuts import render, HttpResponse

from .forms import RegistrationForm

# Create your views here.
def register(requests):
    if requests.method == 'POST':
        form = RegistrationForm(requests.POSTS)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            form = RegistrationForm()
    
    form = RegistrationForm()

    context = {"form":form}

    return render(requests, 'registration/register.html', context)