__author__ = 'Gautam'
from django import forms
from PROFESSOR.models import QuestionDetail

class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionDetail
        fields = '__all__'



"""class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields='__all__'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        #exclude = ['user']
        field='__all__'"""


