__author__ = 'Gautam'

from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ###############Student url####################################
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='student_login'),
    url(r'^student_register$',views.student_register, name='student_register'),
    url(r'^student_login', views.student_login, name='student_login'),
    url(r'^studentlist', views.studentlist, name='studentlist'),
    ###################Professor URL#############################
    url(r'^professor_login', views.professor_login, name='professor_login'),
    url(r'^professor_home', views.professor_home, name='professor_home'),
    url(r'^professor_register$',views.professor_register, name='professor_register'),
    url(r'^professorlist$',views.professorlist,name='professorlist'),
    url(r'^question$', views.question, name='question'),
    url(r'^questionbank$', views.questionbank, name='questionbank'),
    url(r'^createcourse$',views.createcourse,name='createcourse'),
    url(r'^courselist$',views.courselist,name='courselist'),
    url(r'^createassignment$',views.createassignment,name='createassignment'),
    url(r'^assignmentlist$',views.assignmentlist,name='assignmentlist'),
    url(r'^professorcourse$',views.professor_course,name='professor_course'),

    ################Assistant Url################################
    url(r'^assistant_login', views.assistant_login, name='assistant_login'),
    url(r'^assistant_register$',views.assistant_register, name='assistant_register'),
    url(r'^assistantlist$', views.assistantlist, name='assistantlist'),
    ############################################################
    #url(r'^assignment$' , views.assignment, name='assigment')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
