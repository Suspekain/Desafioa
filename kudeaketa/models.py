from django.db import models

# Create your models here.

class Kirolak(models.Model):
    izena = models.CharField(max_length=30)
    azalpena = models.TextField()
    irudia = models.ImageField(default=None, blank=True, null=True)
    created = models.DateTimeField(auto_now=False)
    updated = models.DateTimeField(auto_now=True)
    