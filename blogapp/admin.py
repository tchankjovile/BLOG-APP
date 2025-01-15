from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from blogapp.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nom_category', 'slug')

# Désinscrire le User par défaut
admin.site.unregister(User)

# nous prnom en paraùètre le DefaultUserAdmin parce que nous voulons personnaliser l'affichage des utilisateur
# car ceux ci sont gerer par defaut dans le authUserAdmin
@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    list_display = ('username', 'email', 'password')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display= ('titre', 'auteur', 'etat', 'date_creation', 'category', 'nombre_vue')
    search_fields = ('titre', 'description')
    ordering = ('auteur', 'etat')
    list_filter = ('auteur', 'date_creation', 'date_publication')

@admin.register(Comment)
class comments(admin.ModelAdmin):
    list_display = ['created']