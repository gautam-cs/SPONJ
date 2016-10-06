__author__ = 'Gautam'

from django.shortcuts import render, get_object_or_404
from .models import QuestionDetail

def index(request):
    return render(request,'index.html')

def plogin(request):
    return render(request,'plogin.html')

def psignup(request):
    return render(request,'psignup.html')