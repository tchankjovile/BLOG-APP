from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Model
from django.urls import reverse
from django.conf import settings
from datetime import date
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

# class CustomUser(AbstractUser):
#     sexe_choices = [
#         ("M", "Masculin"),
#         ("F", "Feminin"),
#     ]
#
#     telephone = models.IntegerField( unique=True, null= True, blank = True)
#     sexe = models.CharField(max_length= 8, choices= sexe_choices,null= True, blank= True)
#     def __str__(self):
#         return self.username

class Category(models.Model):
    nom_category = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom_category)  # Utiliser nom_category ici
        super(Category, self).save(*args, **kwargs)  # Appel correct à super

    def __str__(self):
        return self.nom_category

# ma classe manager qui va controler la creation d'un article par un utilisateur
# enfain que celui ci soit vérifier par l'adimistrateur avant sa publication
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(etat= 'publié')

class Article(models.Model):

    etat_choices = [
        ('encours', 'En cours de validation'),
        ('publié', 'publié'),
        ('rejeté', 'rejeté')
    ]

    titre = models.CharField(max_length= 50)
    description= models.TextField()
    image = models.ImageField(upload_to= 'media/', max_length= 120)
    date_creation= models.DateTimeField(auto_now_add= True, editable= False, null=True, blank= True)
    date_modification= models.DateField(default= date.today)
    date_publication= models.DateTimeField(default= timezone.now)
    etat= models.CharField(max_length= 30, choices=etat_choices )
    nombre_vue= models.IntegerField(default= 0, editable= False)
    auteur= models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'articles')
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name='categories')
    likes = models.PositiveIntegerField( default=0)

    objects= models.Manager() # manager par defaut
    publier= PublishedManager()# manager personnalisé

    def get_absolute_url(self):
        return reverse('description', kwargs={"id": str(self.id)})

    def get_modify_url(self):
        return reverse('modify', kwargs={"id": str(self.id)})

    def get_delete_url(self):
        return reverse('delete', kwargs={"id": str(self.id)})

    def __str__(self):
        return self.titre


# class Comment(models.Model):
#     post= models.ForeignKey(Article, on_delete= models.CASCADE, related_name= "comments")
#     # # auteur_com=  models.ForeignKey(User, on_delete=models.CASCADE)
#     # article= models.ForeignKey(Article, on_delete= models.CASCADE, related_name='comments')
#     username= models.CharField(max_length=100)
#     email= models.EmailField(max_length=200)
#     corps = models.TextField(max_length=500)
#     created= models.DateTimeField(auto_now_add= True)
#     updated= models.DateTimeField(auto_now_add= True)
#
#     def __str__(self):
#         return self.article.titre

class Comment(models.Model):
    post= models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    # username= models.CharField(max_length= 100)
    auteur_com= models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentaire')
    email= models.EmailField(max_length= 200)
    body= models.TextField()
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.titre

