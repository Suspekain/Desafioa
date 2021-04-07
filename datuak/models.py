from django.db import models
import datetime

class Kirolaria(models.Model):
    izena = models.CharField(max_length=30)
    abizena = models.CharField(max_length=30)
    jaioterria = models.CharField(max_length=30)
    jaiotze_data = models.DateTimeField
    kirola = models.CharField(max_length=30)
    irudia = models.ImageField(default=None, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
