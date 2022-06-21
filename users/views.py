from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages


from .forms import RegistrationForm, UserEditForm

# Create your views here.
def register(requests):
    if requests.method == 'POST':
        form = RegistrationForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(requests, 'Please correct form and try again')
            form = RegistrationForm()
    
    form = RegistrationForm()

    context = {"form":form}

    return render(requests, 'registration/register.html', context)

def editProfile(requests):

    if requests.user.is_authenticated:
        form = UserEditForm(instance=requests.user)

        if requests.method == 'POST':
            form = UserEditForm(requests.POST, instance=requests.user)
            if form.is_valid():
                form.save()
                return render(requests, 'registration/profile.html')
            else:
                messages.error(requests, 'Please correct form and try again')
                form = UserEditForm()

        context = {'form':form}

        return render(requests, 'registration/editUser.html', context)
    
    else:
        return redirect('login')

def profile(requests):
    return render(requests, 'registration/profile.html')