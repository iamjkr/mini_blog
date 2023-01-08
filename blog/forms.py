from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User

from blog.models import Post


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Enter your password'}))
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Confirm your password'}))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'password1': 'Password',
            'password2': ' confirm Password'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Your First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Your Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Your Email'}),
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Enter Your Username'}))
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control', 'placeholder': 'Enter Your Password'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content']
        labels = {'title': 'Title','content': 'Content'}
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Write a Title'}),
                   'description': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Write Somthing about your...'})}