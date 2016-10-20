__author__ = 'Gautam'
from django import forms
from ACCOUNTS.models import QuestionDetail,ProfessorDetail
from django.contrib.auth.models import User


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionDetail
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('first_name','last_name', 'email','username')

class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = ProfessorDetail
        fields = ('Batch','Interest','Qualification')

