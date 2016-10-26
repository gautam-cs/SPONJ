__author__ = 'Gautam'

from ACCOUNTS.models import QuestionDetail,ProfessorDetail,CourseDetail,AssignmentDetail
from ACCOUNTS.forms import QuestionForm,UserForm,UserProfileForm,CourseForm,AssignmentForm
from django.conf import settings
from django.shortcuts import render, get_object_or_404,render_to_response
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User


def index(request):
    return render (request, "index.html")

############################################PROFESSOR IMPLEMENTATION#######################################################
def professor_login(request):
    context = RequestContext(request)
    user=User.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        #print("auth",str(authenticate(username=username, password=password)))

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('professor_home')
            else:
                return HttpResponse("already login")
        else:
            #print ("please choose your valid username & password: {0}, {1}".format(username, password))
            return HttpResponse("please choose your valid username & password ")
    else:
        return render_to_response('professor/professor_login.html', {}, context)

def professor_logout(request):
    auth.logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

def professor_register(request):
    context = RequestContext(request)
    if request.method == 'POST':
        uf = UserForm(data=request.POST, prefix='user')
        upf = UserProfileForm(data=request.POST, prefix='userprofile')
        if uf.is_valid() * upf.is_valid():
            user=uf.save()
            user.set_password(user.password)
            user.is_admin = True
            user.is_staff = True
            user.is_superuser = False
            user=uf.save()
            userprofile=upf.save(commit=False)
            #userprofile.username(uf.username)
            userprofile.username= user
            userprofile.save()
            return redirect('professorlist')
    else:
        uf=UserForm(prefix='user')
        upf = UserProfileForm(prefix='userprofile')
    return render(request,'professor\professor_register.html', {'uf':uf,'upf':upf}, context)



def professorlist(request):
    professorposts = ProfessorDetail.objects.all()
    userposts=User.objects.all()
    # if request.professorposts.get(username=User.objects.all()):
    # Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [lname])
    """ list = zip(ProfessorDetail.objects.raw('SELECT * FROM ACCOUNTS_ProfessorDetail join ACCOUNTS_User ON'
                                            '(ACCOUNTS_User.username=ACCOUNTS_ProfessorDetail.username)'),
                User.objects.raw(
                    'SELECT * FROM ACCOUNTS_ProfessorDetail join User ON'
                    '(ACCOUNTS_User.username=ACCOUNTS_ProfessorDetail.username)'))"""
    # list=ProfessorDetail.objects.select_related()
    list=zip(professorposts,userposts)
    return render(request, 'professor\professorlist.html', {'list': list})

def professor_home(request):
    Coursepost = CourseDetail.objects.all()
    return render(request, 'professor\professor_home.html', {'Coursepost': Coursepost})

def question(request):
    if request.method=="POST":
        form=QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('qbank')
    else:
        form=QuestionForm()
    return render(request,'professor\question.html',{'form':form})

def questionbank(request):
	QuestionPosts=QuestionDetail.objects.all()
	return render(request, 'professor\questionbank.html',{'QuestionPosts':QuestionPosts})

def createcourse(request):
    if request.method=="POST":
        courseform=CourseForm(request.POST)
        if courseform.is_valid():
            courseform.save()
            return redirect('professor_home')
    else:
        courseform=CourseForm()
    return render(request,'professor\Createcourse.html',{'courseform':courseform})

def courselist(request):
	CoursePosts=CourseDetail.objects.all()
	return render(request, 'professor\courselist.html',{'CoursePosts':CoursePosts})


def createassignment(request):
    if request.method=="POST":
        assignmentform=AssignmentForm(request.POST)
        if assignmentform.is_valid():
            assignmentform.save()
            return redirect('assignmentlist')
    else:
        assignmentform=AssignmentForm()
    return render(request,'professor\createassignment.html',{'assignmentform':assignmentform})


def assignmentlist(request):
	AssignmentPosts=AssignmentDetail.objects.all()
	return render(request, 'professor\assignmentlist.html',{'AssignmentPosts':AssignmentPosts})
###########################################################################################################################


##############################################STUDENT IMPLEMENTATION#######################################################
def student_login(request):
    context = RequestContext(request)
    user = User.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
    if user is not None:
        return HttpResponse("Making is in progress ")

    else:
        return render_to_response('student/student_login.html', {}, context)

def student_logout(request):
    auth.logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

def student_home(request):
    return render (request, "student/student_home.html")

def student_register(request):
    context = RequestContext(request)
    if request.method == 'POST':
        return HttpResponse("Student register page Making is in progress ")
    else:
        uf=UserForm(prefix='user')
        upf = UserProfileForm(prefix='userprofile')
    return HttpResponse("Student register page Making is in progress ")
#############################################################################################################################


##############################################ASSISTANT IMPLEMENTATION#######################################################
def assistant_login(request):
    context = RequestContext(request)
    user = User.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

    else:
        return render_to_response('assistant/assistant_login.html', {}, context)


def assistant_logout(request):
    auth.logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

def assistant_register(request):
    context = RequestContext(request)
    if request.method == 'POST':
        return HttpResponse("Assistant register page Making is in progress ")
    else:
        uf = UserForm(prefix='user')
        upf = UserProfileForm(prefix='userprofile')
    return HttpResponse("Assistant register page Making is in progress ")
############################################################################################################################

