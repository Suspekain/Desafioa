from django.db import models

class Kirolaria(models.Model):
    izena = models.CharField(max_length=30)
    abizena = models.CharField(max_length=30)
    jaioterria = models.CharField(max_length=30)
    jaiotze_data = models.DateTimeField
    kirola = 
    
    
    
    
    
    
    
    izena = models.CharField(max_length=30)
    azalpena = models.TextField()
    irudia = models.ImageField(default=None, blank=True, null=True)
    created = models.DateTimeField(auto_now=False)
    updated = models.DateTimeField(auto_now=True)