from django.urls import path, include
from erregistroa import views
 
urlpatterns = [
    path('erregistratu/', views.erregistratu, name='erregistratu'),
    path('hasi/', views.hasi, name='hasi'),
    path('irten/', views.irten, name='irten'),
]