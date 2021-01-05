from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def erregistratu(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('posts:list')
    else:
        form = UserCreationForm()
    return render(request, 'erregistratu.html', {'form': form})