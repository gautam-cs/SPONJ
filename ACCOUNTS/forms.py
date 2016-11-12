__author__ = 'Gautam'
from django import forms
from ACCOUNTS.models import QuestionDetail,ProfessorDetail,CourseDetail,AssignmentDetail,AssistantDetail,StudentDetail
from django.contrib.auth.models import User
import datetime

######################################################Professor FOrms#############################################
class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionDetail
        fields = '__all__'

class QForm(forms.ModelForm):
    QId = forms.CharField(max_length=20)
    QName = forms.CharField(max_length=20)
    QAuthor = forms.CharField(max_length=20)
    QDescription = forms.CharField(max_length=20)
    #Question = forms.TextField(max_length=200)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('first_name','last_name', 'email','username','password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = ProfessorDetail
        fields = ('Interests','Qualification')

class CourseForm(forms.ModelForm):
    class Meta:
        model=CourseDetail
        fields='__all__'

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = AssignmentDetail
        fields = '__all__'
#################################################Student Forms########################################################
class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('first_name','last_name', 'email','username','password')

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentDetail
        fields = ('Batch','Branch','Programme')
#################################################Assistant FOrms######################################################
class AssistantForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('first_name','last_name', 'email','username','password')

class AssistantProfileForm(forms.ModelForm):
    class Meta:
        model = AssistantDetail
        fields =('TaId','CourseId')