__author__ = 'Gautam'

from ACCOUNTS.models import QuestionDetail,ProfessorDetail,CourseDetail,AssignmentDetail,AssistantDetail,StudentDetail
from ACCOUNTS.forms import QuestionForm,CourseForm,AssignmentForm,AssistantForm,StudentForm ,QForm,ProfessorForm,LoginForm
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
        pf = ProfessorForm(data=request.POST, prefix='professor')
        if pf.is_valid():
            pf.save()
            return redirect('professorlist')
    else:
        pf = ProfessorForm(prefix='professor')
    return render(request, 'professor\professor_register.html', {'pf': pf}, context)


def professorlist(request):
    professorposts = ProfessorDetail.objects.all()
    #list=zip(professorposts,profposts)
    return render(request, 'professor\professorlist.html', {'list': professorposts})

#@login_required
def professor_home(request):
    Coursepost = CourseDetail.objects.all()
    return render(request, 'professor\professor_home.html', {'Coursepost': Coursepost})

def question(request):
    if request.method=="POST":
        form=QuestionForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            newdoc =QuestionDetail(TestCaseInputFile1=request.FILES['docfile'])
            newdoc.save()
            form.save()
            return redirect('questionbank')
    else:
        form=QuestionForm()
    return render(request,'professor\question.html',{'form':form})

def que(request):
    if request.method == 'POST':
        form = QForm(data=request.POST)
        if form.is_valid():
           form.save()
    else:
        form = QuestionForm()
    return render(request, 'professor\Create_Question_Professor.html', {'form': form})

def questionbank(request):
	QuestionPosts=QForm.objects.all()
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
        if sf.is_valid():
            sf.save()
            return redirect('studentlist')
    else:
        sf=StudentForm(prefix='student')
    return render(request,'student\student_register.html', {'sf':sf}, context)


def login(request):
    username = "not logged in"

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            request.session['username'] = username
            s=StudentDetail.objects.filter(SId=username)
            if(s[0].Password!=MyLoginForm.cleaned_data['password']):
                return HttpResponse("Enter valid username & password")

    else:
        MyLoginForm = LoginForm()
        return render(request, 'student/student_login.html')
    return redirect('studentlist')
    #return redirect( request,'test', {"username": username})

def studentlist(request):
    studentposts = StudentDetail.objects.all()
    return render(request, 'student\studentlist.html', {'list': studentposts})

def test(request):
    return HttpResponse('done')

def formView(request):
   if request.session.has_key('username'):
      username = request.session['username']
      return render(request, 'student/studentlist.html', {"username" : username})
   else:
      return render(request, 'student/student_login.html', {})

def professor_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
#############################################################################################################################


##############################################ASSISTANT IMPLEMENTATION#######################################################
def assistant_register(request):
    context = RequestContext(request)
    if request.method == 'POST':
        Af = AssistantForm(data=request.POST, prefix='student')
        if Af.is_valid():
            Af.save()
            return redirect('Assistantlist')
    else:
        Af = AssistantForm(prefix='Assistant')
    return render(request, 'Assistant\Assistant_register.html', {'Af': Af}, context)

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

