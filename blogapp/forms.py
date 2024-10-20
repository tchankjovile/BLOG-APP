from django import forms
from .models import Article, CustomUser


class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'telephone', 'sexe', 'photo', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields= ('titre', 'description', 'image', 'dateCreation', 'nombre_vue', 'auteur')

class ModifyArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields= ('titre', 'description', 'image', 'dateCreation', 'nombre_vue', 'auteur')
