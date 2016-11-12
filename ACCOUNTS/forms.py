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

class ProfessorForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = ProfessorDetail
        fields = ('Name','PId','Email','Password','Interests','Qualification')

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
    Password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = StudentDetail
        fields = ('SId','Name','Email','Password','Batch','Branch','Programme')
#################################################Assistant FOrms######################################################
class AssistantForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=AssistantDetail
        fields=('TaId','CourseId', 'Email','Name','Password')