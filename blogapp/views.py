from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from pyexpat.errors import messages
from django.contrib.auth.models import User
from blogapp.forms import RegistrationForm, ArticleCreateForm, ModifyArticleForm, LoginForm, CommentForm
from blogapp.models import Article, Category, Comment
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse



# Create your views here.
def increment_like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.likes += 1  # Incrémente le compteur de likes
    article.save()
    return JsonResponse({'likes_count': article.likes})  # Retourne le nouveau nombre de likes

def index_view(request, category= None):
    posts= Article.publier.all()
    categorie= Category.objects.all()
    if category:
        category= get_object_or_404(Category, slug=category)
        posts= posts.filter(category= category)

    paginator= Paginator(posts, 5)
    page= request.GET.get('page')
    try:
        posts= paginator.page(page)
    except PageNotAnInteger:
        posts= paginator.page(1)
    except EmptyPage:
        paginator.page(paginator.num_pages)
    context= {
        'posts': posts,
        'page': page,
        'categorie': categorie,
        'category': category
    }
    #print(posts)
    return render(request, 'index.html', context)


@login_required
def home_view(request, category= None):
    posts = Article.publier.all()
    categorie = Category.objects.all()
    if category:
        category = get_object_or_404(Category, slug=category)
        posts = posts.filter(category=category)

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'page': page,
        'categorie': categorie,
        'category': category
    }
    # print(posts)
    return render(request, 'home.html', context)


def listarticle_view(request):
    user  = request.user
    posts= Article.objects.all().filter(auteur= user)
    context= {
        'posts': posts,
    }
    return render(request, 'listarticle.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect, ou utilisateur innexistant ")
        else:
            messages.error(request, "fomulaire mal rempli.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'logout.html', locals())


def signup_view(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user= user_form.save(commit= False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
        else:
            print("formulaire non valide")
            return render(request, 'signup.html', {'user_form': user_form})
    else:
        print("pas de requete post")
        user_form = RegistrationForm()
    return render(request, 'signup.html', {'user_form': user_form})


def description_view(request, id, category= None):
    get_article= get_object_or_404(Article, id=id)
    #incrementer d'un le nmbre de vue d'un article si le boutton j"aime est cliquer
    get_article.nombre_vue=+1
    get_article.save()

    comments= Comment.objects.filter(post= get_article.id)
    new_comment= None
    if request.method== 'POST':
        comment_form= CommentForm(data= request.POST)
        if comment_form.is_valid():
            new_comment= comment_form.save(commit= False)
            new_comment.post= get_article
            new_comment.auteur_com= request.user
            new_comment.save()
    else:
        comment_form= CommentForm()
    # print(get_article)
    # if category:
    #     articlesimilaire= Article.objects.all().filter(category=get_article.category)
    return render(request, 'description.html', locals())


def modify_view(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == 'POST':
        form = ModifyArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('listarticle')
    else:
        form = ModifyArticleForm(instance=article)  # Initialisez le formulaire avec l'instance de l'article

    return render(request, 'modify.html', {'form': form, 'article': article})


def delete_view(request, id):
    article= get_object_or_404(Article, id= id)
    if article.delete():
        return redirect('listarticle')
    return render(request, 'listarticle.html', locals())


@login_required
def articlecreate_view(request):
    form = ArticleCreateForm(request.POST, request.FILES)
    if form.is_valid():
        article= form.save(commit= False)
        article.auteur= request.user
        article.save()
        return redirect('listarticle')
    else:
        form = ArticleCreateForm()
    return render(request, 'articlecreate.html', locals())


def apropos_view(request):
    return render(request, 'apropos.html')


def stream_view(request, id):
    pass