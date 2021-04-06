from django.urls import path, include
from saioa import views
 
urlpatterns = [
    path('', views.erregistratu, name='erregistratu'),
    path('erregistratu/', views.erregistratu, name='erregistratu'),
    path('hasi/', views.hasi, name='hasi'),
    path('irten/', views.irten, name='irten'),
]