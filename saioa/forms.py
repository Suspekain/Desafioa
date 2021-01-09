from django import forms

class formHasi(forms.ModelForm):
    erabiltzailea = forms.TextInput(attrs={'class': 'form-control'})