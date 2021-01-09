from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def erregistratu(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            erabiltzailea = form.cleaned_data['username']
            pasahitza = form.cleaned_data['password1']
            user = authenticate(username=erabiltzailea, password=pasahitza)
            login(request, user)
            return redirect('/k')
    else:
        form = UserCreationForm()
    return render(request, 'saioa/erregistratu.html', {'form': form})

def hasi(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            erabiltzailea = form.cleaned_data['username']
            pasahitza = form.cleaned_data['password']
            user = authenticate(username=erabiltzailea, password=pasahitza)
            login(request, user)
            return redirect('/k')
    else:
        form = AuthenticationForm()
    return render(request, 'saioa/login.html', {'form': form})

def irten(request):
    logout(request)
    return redirect('/')