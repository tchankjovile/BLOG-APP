from django import forms
from django.forms import Textarea

from .models import Article, Comment, Category
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    username= forms.CharField(label="Username", max_length= 100, help_text= '', required= True,
                              widget= forms.TextInput(attrs={"class":"form-control", "id":"username", "type":"text", "placeholder":"username", "data-sb-validations":"required"}))
    first_name= forms.CharField(label="First_name", max_length= 100, help_text= '', required= True,
                              widget= forms.TextInput(attrs={"class":"form-control", "id":"first_name", "type":"text", "placeholder":"First Name", "data-sb-validations":"required"}))
    last_name= forms.CharField(label="Last_name", max_length= 100, help_text= '', required= True,
                              widget= forms.TextInput(attrs={"class":"form-control", "id":"last_name", "type":"text", "placeholder":"Last Name", "data-sb-validations":"required"}))
    email= forms.CharField(label="email", max_length= 100, help_text= '', required= True,
                              widget= forms.TextInput(attrs={"class":"form-control", "id":"email", "type":"email", "placeholder":"email", "data-sb-validations":"required"}))
    password= forms.CharField(label="password", max_length= 100, help_text= '', required= True,
                              widget= forms.TextInput(attrs={"class":"form-control", "id":"password", "type":"password", "placeholder":"password", "data-sb-validations":"required"}))
    confirm_password= forms.CharField(label="confirm_password", max_length= 100, help_text= '', required= True,
                              widget= forms.TextInput(attrs={"class":"form-control", "id":"confirm_password", "type":"password", "placeholder":" confirm password", "data-sb-validations":"required"}))

    # confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password')
        # widgets = {
        #     'password': forms.PasswordInput()
        # }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields= ['titre', 'description', 'image', 'date_modification', 'date_publication', 'etat', 'category']

class ModifyArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields= ('titre', 'description', 'image', 'date_modification', 'category')


class CommentForm(forms.ModelForm):
    # corps= forms.TimeField(widget=Textarea(attrs={'class': 'form-control', 'row':3}))
    class Meta:
        model = Comment
        fields= ('username', 'email', 'corps',)
