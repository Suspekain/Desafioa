from django.urls import path
from orrialdea import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.hasiera, name="Hasiera"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)