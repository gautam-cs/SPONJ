__author__ = 'Gautam'
from django import forms
from PROFESSOR.models import QuestionDetail
from django.contrib.auth.models import User   # fill in custom user info then save it
from django.contrib.auth.forms import UserCreationForm

class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionDetail
        fields = '__all__'



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password')


