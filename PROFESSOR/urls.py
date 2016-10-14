__author__ = 'Gautam'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^logout$', views.logout),
    url(r'^register$',views.register),
    url(r'^question$', views.question, name='question'),
    url(r'^qbank$' ,views.qbank,name='qbank'),
]
