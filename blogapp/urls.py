from django.urls import path

from .views import *

urlpatterns=[
    path('', index_view, name = "index"),
    path('categorie/<slug:category>/', index_view, name='categorylist'),
    path('article/<int:article_id>/like/', increment_like, name='increment_like'),
    path('home/', home_view, name= "home"),
    path('listarticle/', listarticle_view, name= "listarticle"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('createarticle/', articlecreate_view, name="createarticle"),
    path('signup/', signup_view, name= 'signup'),
    path('description/<str:id>/', description_view, name= 'description'),
    path('modify/<str:id>/', modify_view, name= 'modify'),
    path('delete/<str:id>/', delete_view, name= 'delete'),
    path('apropos/', apropos_view, name= 'apropos'),
]