from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings
from datetime import date



# Create your models here.
class CustomUser(AbstractUser):
    telephone = models.IntegerField(null= True, blank = True)
    sexe = models.CharField(max_length= 8, null= True, blank= True)
    photo= models.ImageField(upload_to = 'media/', max_length= 120, null= True, blank= True)
    def __str__(self):
        return self.username


class Article(models.Model):
    titre = models.CharField(max_length= 50)
    description= models.TextField()
    image = models.ImageField(upload_to= 'media/', max_length= 120, null= True, blank= True)
    dateCreation= models.DateField(default= date.today)
    nombre_vue= models.IntegerField(default= 0)
    auteur= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name= 'articles')

    def get_absolute_url(self):
        return reverse('description', kwargs={"id": str(self.id)})

    def get_modify_url(self):
        return reverse('modify', kwargs={"id": str(self.id)})

    def get_delete_url(self):
        return reverse('delete', kwargs={"id": str(self.id)})

    def __str__(self):
        return self.titre