from django.db import models

# Create your models here.

class Contact(models.Model):

    nom = models.CharField(max_lenght=225)
    sujet = models.TextField(max_lenght=225)
    message = models.TextField(max_lenght=700)
    email = models.EmailField()

    date_add = models.DateTimeField(auto_now)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)


    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.nom


class Newslatter(models.Model):

    email = models.EmailField()

    date_add = models.DateTimeField(auto_now)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)


    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.nom

