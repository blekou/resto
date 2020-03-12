from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Compte_social),
admin.site.register(models.Site_info),
admin.site.register(models.Presentation),
admin.site.register(models.Temoignage)

