from django.contrib import admin
from blogapp.models import *


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Article)