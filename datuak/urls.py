from django.urls import path
from datuak import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.hasiera),
    
    # Plantillako elementuak
    path('bubbly', views.bubbly)
    
]