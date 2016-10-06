__author__ = 'Gautam'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^plogin$', views.plogin, name='plogin'),
    url(r'^psignup$', views.psignup, name='psignup'),
    #url(r'^login$', views.login, name='login'),
    #url(r'^addquestion$', views.Question, name='Question'),
]
