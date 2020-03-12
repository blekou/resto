from django.db import models

# Create your models here.

class Compte_social(models.Model):

    nom = models.CharField(max_lenght=70)
    ICONE = [
    ("facebook", "fa-facebook"),
    ("googleplus", "fa-googleplus"),
    ("instagram", "fa-instagram"),
    ("linkedin", "fa-linkedin"),
    ]

    liens = models.URLField()
    icones =models.CharField(choices = ICONE)

    date_add = models.DateTimeField(auto_now)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta():
        verbose_name = "Compte_social"
        verbose_name_plural = "Compte_socials"

    def __str__(self):
        return self.nom


class Site_info(models.Model):

    lien= models.URLField()
    map_url = models.TextField(max_lenght=300)
    email = models.EmailField()
    logo = models.CharField()

    date_add = models.DateTimeField(auto_now)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta():
        verbose_name = "Site_info"
        verbose_name_plural = "Site_infos"

    def __str__(self):
        return self.lien


class Presentation(models.Model):
    nom = models.CharField(max_lenght=225)
    description = models.TextField(max_length= 1000)
    image = models.ImageField()
    video = models.TextField()

    date_add = models.DateTimeField(auto_now)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta():
        verbose_name = "Presentation"
        verbose_name_plural= "Presentations"

    def __str__(self):
        return self.nom

class Temoignage(models.Model):

    photo = models.TextField(max_lenght=225)
    nom = models.CharField(max_length=225)
    prenom = models.CharField(max_length=225)
    message =models.TextField(max_length=225)

    date_add = models.DateTimeField(auto_now)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta():
        verbose_name = "Temoignage"
        verbose_name_plural= "Temoignages"

    def __str__(self):
        return self.nom