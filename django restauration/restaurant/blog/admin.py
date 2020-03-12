from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(CategoriesArticle.models),
admin.site.register(Article.models),
admin.site.register(Commentaire.models),
admin.site.register(Tag.models)