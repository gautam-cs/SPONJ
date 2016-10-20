__author__ = 'Gautam'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user_login', views.user_login, name='plogin'),
    #url(r'^plogin/$','django.contrib.auth.views.login', {'user_login': '/plogin.html'}),
    url(r'^logout$', views.logout),
    url(r'^pregister$',views.pregister, name='pregister'),
    url(r'^professorlist$',views.professorlist,name='professorlist'),
    url(r'^newquestion$', views.question, name='question'),
    url(r'^qbank$' ,views.qbank,name='qbank'),

]
