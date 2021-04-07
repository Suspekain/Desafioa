from django.contrib import admin
from kudeaketa.models import Kirolak
from datuak.models import Kirolaria

# Register your models here.

admin.site.register(Kirolak, Kirolaria)
