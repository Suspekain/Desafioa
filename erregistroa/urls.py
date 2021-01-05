from django.urls import path
from erregistroa import views
 
urlpatterns = [
    path('erregistratu/', views.erregistratu, name='erregistratu')
]