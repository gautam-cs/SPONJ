__author__ = 'Gautam'
from django import forms
from ACCOUNTS.models import *
from django.contrib.auth.models import User
import datetime
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

######################################################Professor FOrms#############################################
class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionDetail
        fields = '__all__'


class AssignmentQuestionForm(forms.ModelForm):
    class Meta:
        model = AssignmentQuestion
        fields = '__all__'


class ProfessorForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = ProfessorDetail
        fields = ('Name', 'PId', 'Email', 'Password', 'Interests', 'Qualification')


class CourseForm(forms.ModelForm):
    StartDate = forms.DateTimeField(widget=forms.SelectDateWidget, initial=datetime.date.today())
    EndDate = forms.DateTimeField(widget=forms.SelectDateWidget, initial=datetime.date.today())

    class Meta:
        model = CourseDetail
        fields = ('CourseId', 'Year', 'CourseName', 'Description', 'StartDate', 'EndDate', 'PId', 'Semester')


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = AssignmentDetail
        fields = '__all__'


class ProfessorLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_message(self):
        username = self.cleaned_data.get("username")
        dbuser = ProfessorDetail.objects.filter(name=username)

        if not dbuser:
            raise forms.ValidationError("User does not exist in our db!")
        return username


class CourseStudentForm(forms.ModelForm):
    class Meta:
        model = Course_student
        fields = '__all__'


class CourseTaForm(forms.ModelForm):
    class Meta:
        model = Courses_Ta
        fields = '__all__'


#################################################Student Forms########################################################
class StudentForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = StudentDetail
        fields = ('SId', 'Name', 'Email', 'Password', 'Batch', 'Branch', 'Programme')



class StudentLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_message(self):
        username = self.cleaned_data.get("username")
        dbuser = StudentDetail.objects.filter(name=username)

        if not dbuser:
            raise forms.ValidationError("User does not exist in our db!")
        return username


#################################################Assistant FOrms######################################################
class AssistantForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = AssistantDetail
        fields = ('TaId', 'CourseId', 'Email', 'Name', 'Password')


class AssistantLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_message(self):
        username = self.cleaned_data.get("username")
        dbuser = AssistantDetail.objects.filter(name=username)

        if not dbuser:
            raise forms.ValidationError("User does not exist in our db!")
        return username
