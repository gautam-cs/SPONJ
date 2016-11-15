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
import os


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
    return render(request, 'professor/professor_register.html', {'pf': pf}, context)


def course_student(request,cid):
    context=RequestContext(request)
    if request.method=='POST':
        csf=CourseStudentForm(data=request.POST,prefix='student')
        if csf.is_valid():
            csf.save()
            return redirect(professor_course,cid)
    else:
        csf = CourseStudentForm(prefix='student')
    return render(request, 'professor/coursestudent.html', {'csf': csf}, context)

def course_ta(request,cid):
    context=RequestContext(request)
    if request.method=='POST':
        ctf=CourseTaForm(data=request.POST,prefix='ta')
        if ctf.is_valid():
            ctf.save()
            return redirect(professor_course,cid)
    else:
        ctf = CourseStudentForm(prefix='ta')
    return render(request, 'professor/courseta.html', {'ctf': ctf}, context)

def professorlist(request):
    professorposts = ProfessorDetail.objects.all()
    #list=zip(professorposts,profposts)
    return render(request, 'professor/professorlist.html', {'list': professorposts})

#@login_required
def professor_home(request):
    if request.session.has_key('username'):
        pid = request.session['username']
        Coursepost = CourseDetail.objects.filter(PId=pid)
        return render(request, 'professor/professor_home.html', {'Coursepost': Coursepost})
    return HttpResponse("Not Logged in")


def question(request):
    if request.method=="POST":
        form=QuestionForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('questionbank')
    else:
        form=QuestionForm()
    return render(request,'professor/question.html',{'form':form})

def question_as(request,asid):
    if request.method=="POST":
        form=QuestionForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            q=form.save()
            ques_ass=AssignmentQuestion(AId_id=asid,QId_id=q.id)
            ques_ass.save()
            return redirect('''/viewassignment/'''+asid)
    else:
        form=QuestionForm()
    return render(request,'professor\question.html',{'form':form})

def questionbank(request):
	QuestionPost=QuestionDetail.objects.all()
	return render(request, 'professor/questionbank.html',{'QuestionPost':QuestionPost})

def createcourse(request):
    if request.method=="POST":
        courseform=CourseForm(request.POST)
        if courseform.is_valid():
            courseform.save()
            return redirect('professor_home')
    else:
        courseform=CourseForm()
    return render(request,'professor/createcourse.html',{'courseform':courseform})

def courselist(request):
	CoursePosts=CourseDetail.objects.all()
	return render(request, 'professor/courselist.html',{'CoursePosts':CoursePosts})

def professor_course(request,cid):
    course=CourseDetail.objects.filter(id=cid)
    professor=ProfessorDetail.objects.filter(PId=course[0].PId)
    assignmentlist=AssignmentDetail.objects.filter(Courseid=course[0].id)
    studentlist=StudentDetail.objects.filter(course_student__CourseId=course[0].id)
    talist=AssistantDetail.objects.filter(courses_ta__CourseId=course[0].id)
    return render(request, 'professor/professor_course.html',
                  {'course':course[0],'assignmentlist':assignmentlist,'talist':talist,'professor_name':professor[0].Name,'studentlist':studentlist})

def specificcourse(request):
	specific_course_post=CourseDetail.objects.all()
	return render(request, 'professor/professor_course.html',{'specific_course_post':specific_course_post})

def createassignment(request,cid):
    if request.method=="POST":
        assignmentform=AssignmentForm(request.POST)
        assignmentform.CreationDate = date.today()
        assignmentform.save()
        if assignmentform.is_valid():
            a=assignmentform.save()
            return redirect('/question/'+str(a.id)+'/')
        else:
            print(assignmentform.errors)

    else:
        assignmentform=AssignmentForm()
    return render(request,'professor/createassignment.html',{'assignmentform':assignmentform,'course':CourseDetail.objects.get(pk=cid)})

def createassignment_and_add_q(request,cid):
    if request.method=="POST":
        assignmentform=AssignmentForm(request.POST)
        #assignmentform.CreationDate = date.today()
        assignmentform.save()
        if assignmentform.is_valid():
            a=assignmentform.save()
            return redirect('question/'+a.id)
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
    return render(request,'professor/viewassignmentprof.html',context={'assignment':assignment,
                                                                       'professor':professor,
                                                                       'languages':languages,
                                                                       'questions':questions})

def view_question(request,aid_qid):
    aid=aid_qid.split("_")[0]
    qid=aid_qid.split("_")[1]
    question=QuestionDetail.objects.get(pk=qid)
    assignment=AssignmentDetail.objects.get(pk=aid)
    course=CourseDetail.objects.get(id=1)
    professor=ProfessorDetail.objects.get(pk=course.PId_id)
    inpf1 = question.TestCaseInputFile1
    inpf1.open(mode='rb')
    inp1 = inpf1.read()
    inpf1.close()
    inpf2 = question.TestCaseInputFile2aa
    inpf2.open(mode='rb')
    inp2 = inpf2.read()
    inpf2.close()
    outf2 = question.OutputFile2
    outf2.open(mode='rb')
    out2 = outf2.read()
    outf2.close()
    outf1 = question.OutputFile1
    outf1.open(mode='rb')
    out1 = outf1.read()
    outf1.close()
    return render(request,'professor/view_question.html',context={'question':question,
                                                                  'assignment':assignment,
                                                                  'inp1':inp1,'inp2':inp2,
                                                                  'out1':out1,'out2':out2,
                                                                  'course':course,"professor":professor})

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
            submissions = Submission.objects.filter(StudentId_id=student.SId,QuestionId_id=question.id)
            if(submissions.count()!=0):
                lastsubmission=submissions.order_by('-SubmissionTime').first()
                q_submissions.append(lastsubmission)
            else:
                q_submissions.append(None)
        dict={"name":student.Name,"submissions":q_submissions,"id":student.SId}
        finalsubmissionlist.append(dict)
    # print(finalsubmissionlist)
    return render(request,'professor/studentvsquestion_matrix.html',context={'assignment':assignment,
                                                                             'course':course,
                                                                             'submissionlist':finalsubmissionlist,
                                                                             'questions':questions})


def view_submission(request,subid):
    lastsubmission=Submission.objects.get(pk=subid)
    question=QuestionDetail.objects.get(pk=lastsubmission.QuestionId_id)
    assignment=AssignmentDetail.objects.get(pk=lastsubmission.AssignmentId_id)
    course=CourseDetail.objects.get(pk=assignment.Courseid_id)
    print(lastsubmission.StudentId_id)
    student=StudentDetail.objects.get(SId=lastsubmission.StudentId_id)
    all_submissions_of_question=Submission.objects.filter(QuestionId_id=lastsubmission.QuestionId_id,StudentId_id=lastsubmission.StudentId_id).order_by('-SubmissionTime')

    return render(request,'professor/view_submissions.html',context={'assignment':assignment,
                                                                     'course':course,
                                                                     'question':question,
                                                                     'submissions':all_submissions_of_question,
                                                                     'student':student})



def professor_login(request):
    username = "not logged in"

    if request.method == "POST":
        # Get the posted form
        professorLoginForm = ProfessorLoginForm(request.POST)

        if professorLoginForm.is_valid():
            username = professorLoginForm.cleaned_data['username']
            request.session['username'] = username
            s=ProfessorDetail.objects.filter(PId=username)
            if(s[0].Password!=professorLoginForm.cleaned_data['password']):
                return HttpResponse("Enter valid username & password")

    else:
        professorLoginForm = ProfessorLoginForm()
        return render(request, 'professor/professor_login.html')
    return redirect('professor_home')

def ProfessorFormView(request):
   if request.session.has_key('username'):
      username = request.session['username']
      return render(request, 'professor/professor_home.html', {"username" : username})
   else:
      return render(request, 'professor/professor_login.html', {})


def Professor_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
###########################################################################################################################


##############################################STUDENT IMPLEMENTATION#######################################################

def student_course(request,cid):
    course=CourseDetail.objects.filter(id=cid)
    professor=ProfessorDetail.objects.filter(PId=course[0].PId)
    assignmentlist=AssignmentDetail.objects.filter(Courseid=course[0].id)
    return render(request, 'student/student_course.html',
                  {'course':course[0],'assignmentlist':assignmentlist,'professor_name':professor[0].Name,})

def student_register(request):
    context = RequestContext(request)
    if request.method == 'POST':
        sf = StudentForm(data=request.POST, prefix='student')
        if sf.is_valid():
            sf.save()
            return redirect('studentlist')
    else:
        sf=StudentForm(prefix='student')
    return render(request,'student/student_register.html', {'sf':sf}, context)


def Student_login(request):
    username = "not logged in"

    if request.method == "POST":
        studentLoginForm = StudentLoginForm(request.POST)

        if studentLoginForm.is_valid():
            username = studentLoginForm.cleaned_data['username']
            request.session['username'] = username
            s=StudentDetail.objects.filter(SId=username)
            if(s[0].Password!=studentLoginForm.cleaned_data['password']):
                return HttpResponse("Enter valid username & password")

        return redirect('student_home')

    else:
        studentLoginForm = StudentLoginForm()
        return render(request, 'student/student_login.html')


def student_home(request):
    if request.session.has_key('username'):
        sid = request.session['username']
        courses = CourseDetail.objects.filter(course_student__SId_id=sid)
        Studentpost = StudentDetail.objects.filter(SId=sid)
        return render(request, 'student/student_home.html', context={'Studentpost': Studentpost,
                                                                         'courses':courses})
    return HttpResponse("Not Logged in")


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
    return render(request, 'student/studentlist.html', {'list': studentposts})
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
    return render(request, 'Assistant/Assistant_register.html', {'Af': Af}, context)

def assistantlist(request):
    assistantposts = AssistantDetail.objects.all()
    asposts=User.objects.all()
    list=zip(assistantposts,asposts)
    return render(request, 'assistant/Assistantlist.html', {'list': list})

def Assistant_login(request):
    username = "not logged in"

    if request.method == "POST":
        # Get the posted form
        assistantLoginForm = AssistantLoginForm(request.POST)

        if assistantLoginForm.is_valid():
            username = assistantLoginForm.cleaned_data['username']
            request.session['username'] = username
            s=AssistantDetail.objects.filter(TaId=username)
            if(s[0].Password!=assistantLoginForm.cleaned_data['password']):
                return HttpResponse("Enter valid username & password")

    else:
        assistantLoginForm =AssistantLoginForm()
        return render(request, 'assistant/Assistant_login.html')
    return redirect('assistant_home')


def assistant_home(request):
    if request.session.has_key('username'):
        taid = request.session['username']
        post =Courses_Ta.objects.get(TaId_id=taid)
        coursepost=CourseDetail.objects.get(id=post.CourseId_id)
        return render(request, 'assistant/Assistant_home.html', {'coursepost': coursepost})
    return HttpResponse("Not Logged in")
############################################################################################################################

