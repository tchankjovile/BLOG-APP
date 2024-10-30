from django.contrib import admin
from blogapp.models import *


# Register your models here.
# admin.site.register(User)
# admin.site.register(Article)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nom_category', 'slug')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display= ('titre', 'auteur', 'etat', 'date_creation', 'category', 'nombre_vue')
    search_fields = ('titre', 'description')
    ordering = ('auteur', 'etat')
    list_filter = ('auteur', 'date_creation', 'date_publication')

@admin.register(Comment)
class comments(admin.ModelAdmin):
    list_display = ['created']