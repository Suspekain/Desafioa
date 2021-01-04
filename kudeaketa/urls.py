from django.urls import path
from kudeaketa import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.hasiera, name="Hasiera"),
    
]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# path('kirolak/', views.kirolak, name="Kirolak"),
#    path('kirolariak/', views.kirolariak, name="Kirolariak"),
#    path('harremana/', views.harremana, name="Harremana"),
#    path('demo1/', views.demo1, name="Demo1"),
#    path('demo2/', views.demo2, name="Demo2"),
#    path('demo3/', views.demo3, name="Demo3"),
#    path('demo4/', views.demo4, name="Demo4"),
#    path('demo5/', views.demo5, name="Demo5"),