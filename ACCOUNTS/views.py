__author__ = 'Gautam'

from ACCOUNTS.models import QuestionDetail,ProfessorDetail,CourseDetail,AssignmentDetail,AssistantDetail,StudentDetail
from ACCOUNTS.forms import QuestionForm,UserForm,UserProfileForm,CourseForm,AssignmentForm,AssistantForm,AssistantProfileForm,\
    StudentForm ,StudentProfileForm
from django.shortcuts import render, get_object_or_404,render_to_response
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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
    return HttpResponseRedirect('/')

def professor_register(request):
    context = RequestContext(request)
    if request.method == 'POST':
        uf = UserForm(data=request.POST, prefix='user')
        upf = UserProfileForm(data=request.POST, prefix='userprofile')
        if uf.is_valid() * upf.is_valid():
            uf=uf.save()
            uf.set_password(uf.password)
            uf.is_admin = True
            uf.is_staff = True
            uf.is_superuser = True
            uf.save()
            userprofile=upf.save(commit=False)
            #userprofile.username(uf.username)
            userprofile.username = User.objects.all()
            userprofile.save()
            return redirect('professorlist')
    else:
        uf=UserForm(prefix='user')
        upf = UserProfileForm(prefix='userprofile')
    return render(request,'professor\professor_register.html', {'uf':uf,'upf':upf}, context)

def professorlist(request):
    professorposts = ProfessorDetail.objects.all()
    profposts=User.objects.all()
    # if request.professorposts.get(username=User.objects.all()):
    # Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [lname])
    """ list = zip(ProfessorDetail.objects.raw('SELECT * FROM ACCOUNTS_ProfessorDetail join ACCOUNTS_User ON'
                                            '(ACCOUNTS_User.username=ACCOUNTS_ProfessorDetail.username)'),
                User.objects.raw(
                    'SELECT * FROM ACCOUNTS_ProfessorDetail join User ON'
                    '(ACCOUNTS_User.username=ACCOUNTS_ProfessorDetail.username)'))"""
    # list=ProfessorDetail.objects.select_related()
    list=zip(professorposts,profposts)
    return render(request, 'professor\professorlist.html', {'list': list})

@login_required
def professor_home(request):
    Coursepost = CourseDetail.objects.filter(username=request.POST.get('username'))
    return render(request, 'professor\professor_home.html', {'Coursepost': Coursepost})

def question(request):
    if request.method=="POST":
        form=QuestionForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form = QuestionDetail(TestCaseInputFile1=request.FILES['TestCaseInputFile1'])
            form.save()
            return redirect('questionbank')
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
    return render(request,'professor\createcourse.html',{'courseform':courseform})

def courselist(request):
	CoursePosts=CourseDetail.objects.all()
	return render(request, 'professor\courselist.html',{'CoursePosts':CoursePosts})

def professor_course(request):
	return render(request, 'professor\professor_course.html')


def specificcourse(request):
	specific_course_post=CourseDetail.objects.all()
	return render(request, 'professor\professor_course.html',{'specific_course_post':specific_course_post})

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
	return render(request, 'professor/assignmentlist.html',{'AssignmentPosts':AssignmentPosts})
###########################################################################################################################


##############################################STUDENT IMPLEMENTATION#######################################################
def student_register(request):
    context = RequestContext(request)
    if request.method == 'POST':
        sf = StudentForm(data=request.POST, prefix='student')
        spf = StudentProfileForm(data=request.POST, prefix='studentprofile')
        if sf.is_valid() * spf.is_valid():
            sf=sf.save()
            sf.set_password(sf.password)
            sf.is_admin = True
            sf.is_staff = True
            sf.is_superuser = False
            sf=sf.save()
            studentprofile=spf.save(commit=False)
            spf.username= sf
            studentprofile.save()
            return redirect('studentlist')
    else:
        sf=StudentForm(prefix='student')
        spf =StudentProfileForm(prefix='studentprofile')
    return render(request,'student\student_register.html', {'sf':sf,'spf':spf}, context)

def studentlist(request):
    studentposts = StudentDetail.objects.all()
    stposts=User.objects.all()
    list=zip(studentposts,stposts)
    return render(request, 'student\studentlist.html', {'list': list})

def student_login(request):
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
                return HttpResponseRedirect('studentlist')
            else:
                return HttpResponse("already login")
        else:
            #print ("please choose your valid username & password: {0}, {1}".format(username, password))
            return HttpResponse("please choose your valid username & password ")
    else:
        return render_to_response('student/student_login.html', {}, context)

def professor_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
#############################################################################################################################


##############################################ASSISTANT IMPLEMENTATION#######################################################
def assistant_register(request):
    context = RequestContext(request)
    if request.method == 'POST':
        af = AssistantForm(data=request.POST, prefix='assistant')
        apf = AssistantProfileForm(data=request.POST, prefix='assistantprofile')
        if af.is_valid() * apf.is_valid():
            af=af.save()
            af.set_password(af.password)
            af.is_admin = True
            af.is_staff = True
            af.is_superuser = False
            af=af.save()
            assistantprofile=apf.save(commit=False)
            apf.username= af
            assistantprofile.save()
            return redirect("assistantlist")
    else:
        af=AssistantForm(prefix='assistant')
        apf =AssistantProfileForm(prefix='assistantprofile')
    return render(request,'assistant\Assistant_register.html', {'af':af,'apf':apf}, context)

def assistantlist(request):
    assistantposts = AssistantDetail.objects.all()
    asposts=User.objects.all()
    list=zip(assistantposts,asposts)
    return render(request, 'assistant\Assistantlist.html', {'list': list})

def assistant_login(request):
    context = RequestContext(request)
    user=User.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('assistantlist')
            else:
                return HttpResponse("already login")
        else:
            return HttpResponse("please choose your valid username & password ")
    else:
        return render_to_response('assistant/assistant_login.html', {}, context)

def professor_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
############################################################################################################################

