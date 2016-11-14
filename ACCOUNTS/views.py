__author__ = 'Gautam'

from ACCOUNTS.models import *
from ACCOUNTS.forms import *
from django.shortcuts import render, get_object_or_404,render_to_response
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import date
from django.contrib.auth.models import User

def index(request):
    return render (request, "index.html")

############################################PROFESSOR IMPLEMENTATION#######################################################
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
    if request.session.has_key('username'):
        pid = request.session['username']
        Coursepost = CourseDetail.objects.filter(PId=pid)
        print(Coursepost[0])
        return render(request, 'professor\professor_home.html', {'Coursepost': Coursepost})
    return HttpResponse("Not Logged in")


def question(request):
    if request.method=="POST":
        form=QuestionForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('questionbank')
    else:
        form=QuestionForm()
    return render(request,'professor\question.html',{'form':form})

def questionbank(request):
	QuestionPost=QuestionDetail.objects.all()
	return render(request, 'professor\questionbank.html',{'QuestionPost':QuestionPost})

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

def professor_course(request,cid):
    course=CourseDetail.objects.filter(id=cid)
    professor=ProfessorDetail.objects.filter(PId=course[0].PId)
    assignmentlist=AssignmentDetail.objects.filter(Courseid=course[0].id)
    studentlist=StudentDetail.objects.filter(course_student__CourseId=course[0].id)
    talist=AssistantDetail.objects.filter(courses_ta__CourseId=course[0].id)
    return render(request, 'professor\professor_course.html',
                  {'course':course[0],'assignmentlist':assignmentlist,'talist':talist,'professor_name':professor[0].Name,'studentlist':studentlist})

def specificcourse(request):
	specific_course_post=CourseDetail.objects.all()
	return render(request, 'professor\professor_course.html',{'specific_course_post':specific_course_post})

def createassignment(request,cid):
    if request.method=="POST":
        assignmentform=AssignmentForm(request.POST)
        #assignmentform.CreationDate = date.today()
        assignmentform.save()
        if assignmentform.is_valid():
            assignmentform.save()
            return redirect('assignmentlist')
        else:
            print(assignmentform.errors)

    else:
        assignmentform=AssignmentForm()
    return render(request,'professor\createassignment.html',{'assignmentform':assignmentform,'course':CourseDetail.objects.get(pk=cid)})


def view_assignment(request,asid):
    assignment=AssignmentDetail.objects.get(pk=asid)
    professor=ProfessorDetail.objects.get(pk=request.session['username'])
    languages=Assignment_languages.objects.filter(AssignmentId=asid)
    questions=QuestionDetail.objects.filter(assignmentquestion__AId=asid)
    return render(request,'professor/viewassignmentprof.html',context={'assignment':assignment,'professor':professor,'languages':languages,'questions':questions})


def assignmentlist(request):
	AssignmentPosts=AssignmentDetail.objects.all()
	return render(request, 'professor/assignmentlist.html',{'AssignmentPosts':AssignmentPosts})

def studentvsques_matrix(request,asid):
    assignment=AssignmentDetail.objects.get(pk=asid)
    course=CourseDetail.objects.get(id=assignment.Courseid_id)
    finalsubmissionlist=[]
    studentlist=StudentDetail.objects.filter(course_student__CourseId=course.id)
    questions = QuestionDetail.objects.filter(assignmentquestion__AId=asid)
    print(questions)
    for student in studentlist:
        q_submissions=[]
        for question in questions:
            submissions = Submission.objects.filter(StudentId_id=student.SId,QuestionId_id=question.Qid)
            if(submissions.count()!=0):
                lastsubmission=submissions.order_by('-SubmissionTime').first()
                q_submissions.append(lastsubmission)
            else:
                q_submissions.append(None)
        dict={"name":student.Name,"submissions":q_submissions,"id":student.SId}
        finalsubmissionlist.append(dict)
    print(finalsubmissionlist)
    return render(request,'professor/studentvsquestion_matrix.html',context={'assignment':assignment,
                                                                             'course':course,
                                                                             'submissionlist':finalsubmissionlist,
                                                                             'questions':questions})
def view_submission(request,subid):
    return HttpResponse(subid)
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


def professor_login(request):
    username = "not logged in"

    if request.method == "POST":
        # Get the posted form
        ProfessorLoginForm = StudentLoginForm(request.POST)

        if ProfessorLoginForm.is_valid():
            username = ProfessorLoginForm.cleaned_data['username']
            request.session['username'] = username
            s=ProfessorDetail.objects.filter(PId=username)
            if(s[0].Password!=ProfessorLoginForm.cleaned_data['password']):
                return HttpResponse("Enter valid username & password")

    else:
        ProfessorLoginForm = StudentLoginForm()
        return render(request, 'professor/professor_login.html')
    return redirect('professor_home')

def ProfessorFormView(request):
   if request.session.has_key('username'):
      username = request.session['username']
      return render(request, 'professor/professor_home.html', {"username" : username})
   else:
      return render(request, 'student/student_login.html', {})

def Professor_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
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


def Student_login(request):
    username = "not logged in"

    if request.method == "POST":
        # Get the posted form
        MyStudentLoginForm = StudentLoginForm(request.POST)

        if StudentLoginForm.is_valid():
            username = StudentLoginForm.cleaned_data['username']
            request.session['username'] = username
            s=StudentDetail.objects.filter(SId=username)
            if(s[0].Password!=StudentLoginForm.cleaned_data['password']):
                return HttpResponse("Enter valid username & password")

    else:
        MyStudentLoginForm = StudentLoginForm()
        return render(request, 'student/student_login.html')
    return redirect('studentlist')

def StudentFormView(request):
   if request.session.has_key('username'):
      username = request.session['username']
      return render(request, 'student/studentlist.html', {"username" : username})
   else:
      return render(request, 'student/student_login.html', {})

def Student_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def studentlist(request):
    studentposts = StudentDetail.objects.all()
    return render(request, 'student\studentlist.html', {'list': studentposts})
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

def Assistant_login(request):
    username = "not logged in"

    if request.method == "POST":
        # Get the posted form
        MyAssistantLoginForm = AssistantLoginForm(request.POST)

        if AssistantLoginForm.is_valid():
            username = AssistantLoginForm.cleaned_data['username']
            request.session['username'] = username
            s=ProfessorDetail.objects.filter(PId=username)
            if(s[0].Password!=AssistantLoginForm.cleaned_data['password']):
                return HttpResponse("Enter valid username & password")

    else:
        MyAssistantLoginForm =AssistantLoginForm()
        return render(request, 'assistant/Assistant_login.html')
    return redirect('professor_home')

def ProfessorFormView(request):
   if request.session.has_key('username'):
      username = request.session['username']
      return render(request, 'professor/professor_home.html', {"username" : username})

   else:
      return render(request, 'student/student_login.html', {})
############################################################################################################################

