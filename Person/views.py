from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # redirige vers une page existante (ex: page d'accueil)
        else:
            print(form.errors)  # utile pour déboguer
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def home(request):
    return render(request, 'home.html')