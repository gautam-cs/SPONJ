__author__ = 'Gautam'

from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ###############Student url####################################
    url(r'^connection$', views.StudentFormView, name ='loginform'),
    url(r'^$', views.Student_login, name='login'),
    url(r'^student_register$',views.student_register, name='student_register'),
    url(r'^student_home$', views.student_home, name='student_home'),
    url(r'^studentlist$', views.studentlist, name='studentlist'),
    url(r'^studentcourse/(?P<cid>([A-Za-z0-9]+))/$', views.student_course, name='student_course'),
    url(r'^viewassignment_student/(?P<asid>([A-Za-z0-9]+))/$', views.view_assignment_student, name='view_assignment_stud'),
    url(r'^viewquestion_student/(?P<aid_qid>([A-Za-z0-9_]+))/$', views.view_question_student, name='view_question'),

                  ###################Professor URL#############################
    url(r'^professor_login$', views.professor_login, name='professor_login'),
    url(r'^professor_home$', views.professor_home, name='professor_home'),
    url(r'^professor_register$',views.professor_register, name='professor_register'),
    url(r'^professorlist$',views.professorlist,name='professorlist'),
    url(r'^question$', views.question, name='question'),
    url(r'^question/(?P<asid>([A-Za-z0-9]+))/$', views.question_as, name='question_as'),
    url(r'^questionbank$', views.questionbank, name='questionbank'),
    url(r'^createcourse$',views.createcourse,name='createcourse'),
    url(r'^courselist$',views.courselist,name='courselist'),
    url(r'^coursestudent/(?P<cid>([A-Za-z0-9]+))/$',views.course_student,name='coursestudent'),
    url(r'^courseta/(?P<cid>([A-Za-z0-9]+))/$',views.course_ta,name='courseta'),
    url(r'^createassignment/(?P<cid>([A-Za-z0-9]+))/$',views.createassignment,name='createassignment'),
    url(r'^createassignment_q/(?P<cid>([A-Za-z0-9]+))/$',views.createassignment_and_add_q,name='createassignmentwithq'),
    url(r'^assignmentlist$',views.assignmentlist,name='assignmentlist'),
    url(r'^professorcourse/(?P<cid>([A-Za-z0-9]+))/$',views.professor_course,name='professor_course'),
    url(r'^viewassignment/(?P<asid>([A-Za-z0-9]+))/$',views.view_assignment,name='view_assignmentprof'),
    url(r'^viewquestion/(?P<aid_qid>([A-Za-z0-9_]+))/$',views.view_question,name='view_question'),
    url(r'^viewsubmission/(?P<subid>([A-Za-z0-9]+))/$',views.view_submission,name='view_submissionprof'),
    url(r'^studentvsquestion_matrix/(?P<asid>([A-Za-z0-9]+))/$',views.studentvsques_matrix,name='view_studentvsquestion_matrix'),
    url(r'^professorcourse$', views.professor_course, name='professor_course'),



    ################Assistant Url################################
    url(r'^assistant_login$', views.Assistant_login, name='Assistant_login'),
    url(r'^assistant_register$',views.assistant_register, name='assistant_register'),
    url(r'^assistantlist$', views.assistantlist, name='assistantlist'),
    url(r'^assistant_home/(?P<taid>([A-Za-z0-9]+))/$', views.assistant_home, name='assistant_home'),
    ############################################################
    #url(r'^assignment$' , views.assignment, name='assigment')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)