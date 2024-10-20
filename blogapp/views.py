from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from pyexpat.errors import messages
from blogapp.forms import SignupForm, ArticleCreateForm, ModifyArticleForm, LoginForm
from blogapp.models import Article, CustomUser
from django.contrib import messages
# Create your views here.


def index_view(request):
    posts= Article.objects.all()
    #print(posts)
    return render(request, 'index.html', locals())


@login_required
def home_view(request):
    user  = request.user
    posts= Article.objects.filter(auteur= user)
    context= {
        'posts': posts,
    }
    return render(request, 'home.html', context)


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
    if request.method == "POST":
        user_form = SignupForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
         user_form = SignupForm()
    return render(request, 'signup.html', {'user_form': user_form})


def description_view(request, id):
    get_article= get_object_or_404(Article, id=id)
    print(get_article)
    return render(request, 'description.html', locals())


def modify_view(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == 'POST':
        form = ModifyArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ModifyArticleForm(instance=article)  # Initialisez le formulaire avec l'instance de l'article

    return render(request, 'modify.html', {'form': form, 'article': article})


def delete_view(request, id):
    article= get_object_or_404(Article, id= id)
    if article.delete():
        return redirect('home')
    return render(request, 'home.html', locals())

def articlecreate_view(request):
    form = ArticleCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleCreateForm()
        messages= "votre article a été enregistrer"
    return render(request, 'articlecreate.html', locals())
def apropos_view(request):
    return render(request, 'apropos.html')