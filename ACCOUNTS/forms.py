__author__ = 'Gautam'
from django import forms
from ACCOUNTS.models import QuestionDetail,ProfessorDetail,CourseDetail,AssignmentDetail,AssistantDetail,StudentDetail
from django.contrib.auth.models import User
import datetime

######################################################Professor FOrms#############################################
class QuestionForm(forms.ModelForm):
    TestCaseInputFile1 = forms.FileField(
        label='Select a file',)
        #help_text='max. 42 megabytes')
    class Meta:
        model = QuestionDetail
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('first_name','last_name', 'email','username','password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = ProfessorDetail
        fields = ('Batch','Interests','Qualification')

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
        fields = ('Batch','Branch','Programme','SiD')
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