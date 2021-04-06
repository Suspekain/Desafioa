from django.shortcuts import render

# Create your views here.

def hasiera(request):
    return render(request, "datuak/hasiera.html")

def apostuak(request):
    return render(request, 'datuak/apostuak.html')

def bubbly(request):
    return render(request, 'datuak/bubbly.html')