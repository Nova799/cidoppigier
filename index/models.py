from django.db import models
from datetime import date

# Create your models here.

class Users(models.Model):
    idfy = models.CharField(max_length=100)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=100)
    addrMail = models.CharField(max_length=100)
    loginMail = models.CharField(max_length=100, unique=True)
    mdp = models.CharField(max_length=12)
    filiere = models.CharField(max_length=10)
    typeOfUser = models.CharField(max_length=5, default = "user")
    state = models.BooleanField(default=True)
    elligible = models.BooleanField(default=True)

    def __str__(self):
        return "{} {}".format(self.nom, self.prenom)

class Documents(models.Model):
    idfy = models.CharField(max_length=50)
    titre = models.CharField(max_length=50)
    typeOfDoc = models.CharField(max_length=50)
    resume = models.TextField()
    auteur = models.CharField(max_length=100)
    physique = models.BooleanField(default=False)
    emplacement = models.CharField(default="", max_length=150, null=True)
    reservedby = models.CharField(default="", max_length=400)
    isbn = models.CharField(default="", max_length = 150, unique=True)
    file_path = models.FileField(upload_to="docs/", null=True)
    disponible = models.BooleanField(default=True)
    existe = models.BooleanField(default=True)
    avg = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.titre)

class Appreciations(models.Model):
    note = models.IntegerField(default=0)
    book = models.ForeignKey(Documents, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.book.titre
    
class Emprunts(models.Model):
    idfy = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    book = models.ForeignKey(Documents, on_delete=models.CASCADE)
    dateEmprunt = models.DateField(default=date.today)
    dateRetour = models.DateField(null=True)
    regle = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.book.titre}"

class xls(models.Model):
    xls_file =  models.FileField(upload_to = "xls_file/", null = True)