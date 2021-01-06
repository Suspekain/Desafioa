from django.shortcuts import render

# Create your views here.

def hasiera(request):
    return render(request, "kudeaketa/hasiera.html")
