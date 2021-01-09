from django.shortcuts import render

# Create your views here.

def hasiera(request):
    return render(request, "kudeaketa/hasiera.html")

def apostuak(request):
    return render(request, 'kudeaketa/apostuak.html')

def bubbly(request):
    return render(request, 'kudeaketa/bubbly.html')
