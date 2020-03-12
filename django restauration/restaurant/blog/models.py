from django.db import models

# Create your models here.

#models categories articles
class CategoriesArticle(models.Model):

    nom = models.CharField(max_lenght=225)
    description = models.TextField(max_lenght=225)
    image = models.ImageField()

    date_add = models.DateTimeField(auto_now)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)


    class Meta:
        verbose_name = "CategoriesArticle"
        verbose_name_plural = "CategoriesArticles"

    def __str__(self):
        return self.nom


#models articles
class Article(models.Model):

    titre = models.CharField(max_lenght=225)
    description = models.TextField(max_lenght=225)
    image = models.ImageField(upload_to="images/Article")
    contenu = models.TextField(max_lenght=225)
    categories_articles = models.ForeignKey(categories, on_delete=models.CASCADE, related_name="image/Article")
    tag = models.CharField()

    date_add = models.DateTimeField(auto_now)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)


    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.titre+self.description

#models commentaires
class Commentaire(models.Model):

    nom = models.CharField(max_lenght=225)
    prenom = models.CharField(max_lenght=225)
    commentaire = models.TextField(max_lenght=225)
    article = models.ForeignKey(categories, on_delete=models.CASCADE, related_name="image/Article")

    date_add = models.DateTimeField(auto_now)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)


    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"

    def __str__(self):
        return self.nom

#models tag
class Tag(models.Model):

    nom = models.CharField(max_lenght=225)
    description = models.TextField(max_lenght=225)

    date_add = models.DateTimeField(auto_now)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)


    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.nom