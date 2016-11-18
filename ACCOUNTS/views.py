__author__ = 'Gautam'

from ACCOUNTS.models import *
from ACCOUNTS.forms import *
from django.shortcuts import render, get_object_or_404, render_to_response
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import date
from django.contrib.auth.models import User
import os
from subprocess import call


def index(request):
    return render(request, "index.html")


############################################PROFESSOR IMPLEMENTATION#######################################################
def professor_register(request):
    context = RequestContext(request)
    if request.method == 'POST':
        pf = ProfessorForm(data=request.POST, prefix='professor')
        if pf.is_valid():
            pf.save()
            return redirect('/')
    else:
        pf = ProfessorForm(prefix='professor')
    return render(request, 'professor/professor_register.html', {'pf': pf}, context)


def course_student(request, cid):
    if request.session.has_key('username'):
        pid = request.session['username']
        Coursepost = CourseDetail.objects.filter(PId=pid)
        data = []
        for course in Coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)
        context = RequestContext(request)
        if request.method == 'POST':
            csf = CourseStudentForm(data=request.POST, prefix='student')
            if csf.is_valid():
                csf.save()
                return redirect(professor_course, cid)
        else:
            csf = CourseStudentForm(prefix='student')
        return render(request, 'professor/coursestudent.html', {'csf': csf, 'data': data}, context)
    return HttpResponse("Not Logged in")


def course_ta(request, cid):
    if request.session.has_key('username'):
        pid = request.session['username']
        Coursepost = CourseDetail.objects.filter(PId=pid)
        data = []
        for course in Coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)
        context = RequestContext(request)
        if request.method == 'POST':
            ctf = CourseTaForm(data=request.POST, prefix='ta')
            if ctf.is_valid():
                ctf.save()
                return redirect(professor_course, cid)
        else:
            ctf = CourseStudentForm(prefix='ta')
        return render(request, 'professor/courseta.html', {'ctf': ctf, 'data': data}, context)
    return HttpResponse("Not Logged in")


def professorlist(request):
    if request.session.has_key('username'):
        professorposts = ProfessorDetail.objects.all()
        # list=zip(professorposts,profposts)
        return render(request, 'professor/professorlist.html', {'list': professorposts})
    return HttpResponse("Not Logged in")


    # @login_required


def question(request):
    if request.session.has_key('username'):
        pid = request.session['username']
        Coursepost = CourseDetail.objects.filter(PId=pid)
        data = []
        for course in Coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)
        if request.method == "POST":
            form = QuestionForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                form.save()
                return redirect('questionbank')
        else:
            form = QuestionForm()
        return render(request, 'professor/question.html', {'form': form, 'data': data})
    return HttpResponse("Not Logged in")


def question_as(request, asid):
    if request.session.has_key('username'):
        pid = request.session['username']
        Coursepost = CourseDetail.objects.filter(PId=pid)
        data = []
        for course in Coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)
        if request.method == "POST":
            form = QuestionForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                q = form.save()
                ques_ass = AssignmentQuestion(AId_id=asid, QId_id=q.id)
                ques_ass.save()
                return redirect('''/viewassignment/''' + asid)
        else:
            form = QuestionForm()
        return render(request, 'professor/question.html', {'form': form, 'data': data})
    return HttpResponse("Not Logged in")


def questionbank(request):
    if request.session.has_key('username'):
        QuestionPost = QuestionDetail.objects.all()
        return render(request, 'professor/questionbank.html', {'QuestionPost': QuestionPost})
    return HttpResponse("Not Logged in")


def createcourse(request):
    if request.session.has_key('username'):
        pid = request.session['username']
        Coursepost = CourseDetail.objects.filter(PId=pid)
        data = []
        for course in Coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)
        if request.method == "POST":
            courseform = CourseForm(request.POST)
            if courseform.is_valid():
                courseform.save()
                return redirect('professor_home')
        else:
            courseform = CourseForm()
        return render(request, 'professor/createcourse.html', {'courseform': courseform, 'data': data})
    return HttpResponse("Not Logged in")


def courselist(request):
    if request.session.has_key('username'):
        CoursePosts = CourseDetail.objects.all()
        return render(request, 'professor/courselist.html', {'CoursePosts': CoursePosts})
    return HttpResponse("Not Logged in")


def professor_course(request, cid):
    if request.session.has_key('username'):
        pid = request.session['username']
        Coursepost = CourseDetail.objects.filter(PId=pid)
        data = []
        for course in Coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)
        course = CourseDetail.objects.filter(id=cid)
        professor = ProfessorDetail.objects.filter(PId=course[0].PId)
        assignmentlist = AssignmentDetail.objects.filter(Courseid=course[0].id)
        studentlist = StudentDetail.objects.filter(course_student__CourseId=course[0].id)
        talist = AssistantDetail.objects.filter(courses_ta__CourseId=course[0].id)
        return render(request, 'professor/professor_course.html',
                      {'course': course[0], 'assignmentlist': assignmentlist, 'talist': talist,
                       'professor_name': professor[0].Name, 'studentlist': studentlist, 'data': data})
    return HttpResponse("Not Logged in")


def assistant_register(request, cid):
    context = RequestContext(request)
    if request.method == 'POST':
        Af = AssistantForm(data=request.POST, prefix='assistant')
        if Af.is_valid():
            temp = Af.save()
            ta = Courses_Ta(CourseId_id=cid, TaId_id=temp.TaId)
            ta.save()
            course = CourseDetail.objects.filter(id=cid)
            talist = AssistantDetail.objects.filter(courses_ta__CourseId=course[0].id)
            return redirect('/professorcourse/' + cid)
    else:
        Af = AssistantForm(prefix='assistant')
    return render(request, 'assistant/assistant_register.html', {'Af': Af,}, context)


def createassignment(request, cid):
    if request.session.has_key('username'):
        pid = request.session['username']
        Coursepost = CourseDetail.objects.filter(PId=pid)
        data = []
        for course in Coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)
        if request.method == "POST":
            assignmentform = AssignmentForm(request.POST)
            assignmentform.save()
            if assignmentform.is_valid():
                a = assignmentform.save()
                return redirect('/question/' + str(a.id) + '/')
            else:
                print(assignmentform.errors)

        else:
            assignmentform = AssignmentForm()
        return render(request, 'professor/createassignment.html'
                      , {'assignmentform': assignmentform, 'course': CourseDetail.objects.get(pk=cid), 'data': data})
    return HttpResponse("Not Logged in")


def createassignment_and_add_q(request, cid):
    if request.session.has_key('username'):
        pid = request.session['username']
        Coursepost = CourseDetail.objects.filter(PId=pid)
        data = []
        for course in Coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)
        if request.method == "POST":
            assignmentform = AssignmentForm(request.POST)
            assignmentform.CreationDate = date.today()
            assignmentform.save()
            if assignmentform.is_valid():
                a = assignmentform.save()
                return redirect('question/' + a.id)
            else:
                print(assignmentform.errors)

        else:
            assignmentform = AssignmentForm()
        return render(request, 'professor/createassignment.html'
                      , {'assignmentform': assignmentform, 'course': CourseDetail.objects.get(pk=cid), 'data': data})
    return HttpResponse("Not Logged in")


def view_assignment(request, asid):
    if request.session.has_key('username'):
        pid = request.session['username']
        Coursepost = CourseDetail.objects.filter(PId=pid)
        data = []
        for course in Coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)
        assignment = AssignmentDetail.objects.get(pk=asid)
        professor = ProfessorDetail.objects.get(pk=CourseDetail.objects.get(id=assignment.Courseid_id).PId_id)
        languages = Assignment_languages.objects.filter(AssignmentId=asid)
        questions = QuestionDetail.objects.filter(assignmentquestion__AId=asid)
        return render(request, 'professor/viewassignmentprof.html', context={'assignment': assignment,
                                                                             'professor': professor,
                                                                             'languages': languages,
                                                                             'questions': questions,
                                                                             'data': data})
    return HttpResponse("Not Logged in")


def view_question(request, aid_qid):
    if request.session.has_key('username'):
        sid = request
        pid = request.session['username']
        Coursepost = CourseDetail.objects.filter(PId=pid)
        data = []
        for course in Coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)
        aid = aid_qid.split("_")[0]
        qid = aid_qid.split("_")[1]
        question = QuestionDetail.objects.get(pk=qid)
        assignment = AssignmentDetail.objects.get(pk=aid)
        course = CourseDetail.objects.get(id=1)
        professor = ProfessorDetail.objects.get(pk=course.PId_id)
        inpf1 = question.TestCaseInputFile1
        inpf1.open(mode='rb')
        inp1 = inpf1.read()
        inpf1.close()
        inpf2 = question.TestCaseInputFile2
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
        return render(request, 'professor/view_question.html', context={'question': question,
                                                                        'assignment': assignment,
                                                                        'inp1': inp1, 'inp2': inp2,
                                                                        'out1': out1, 'out2': out2,
                                                                        'course': course, "professor": professor
            , 'data': data})
    return HttpResponse("Not Logged in")


def assignmentlist(request):
    if request.session.has_key('username'):
        AssignmentPosts = AssignmentDetail.objects.all()
        return render(request, 'professor/assignmentlist.html', {'AssignmentPosts': AssignmentPosts})
    return HttpResponse("Not Logged in")


def studentvsques_matrix(request, asid):
    if request.session.has_key('username'):
        pid = request.session['username']
        Coursepost = CourseDetail.objects.filter(PId=pid)
        data = []
        for course in Coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)
        assignment = AssignmentDetail.objects.get(pk=asid)
        course = CourseDetail.objects.get(id=assignment.Courseid_id)
        finalsubmissionlist = []
        studentlist = StudentDetail.objects.filter(course_student__CourseId=course.id)
        questions = QuestionDetail.objects.filter(assignmentquestion__AId=asid)
        print(questions)
        for student in studentlist:
            q_submissions = []
            for question in questions:
                submissions = Submission.objects.filter(StudentId_id=student.SId, QuestionId_id=question.id)
                if (submissions.count() != 0):
                    lastsubmission = submissions.order_by('-SubmissionTime').first()
                    q_submissions.append(lastsubmission)
                else:
                    q_submissions.append(None)
            dict = {"name": student.Name, "submissions": q_submissions, "id": student.SId}
            finalsubmissionlist.append(dict)
    # print(finalsubmissionlist)
    return render(request, 'professor/studentvsquestion_matrix.html', context={'assignment': assignment,
                                                                               'course': course,
                                                                               'submissionlist': finalsubmissionlist,
                                                                               'questions': questions,
                                                                               'data': data})


def view_submission(request, subid):
    if request.session.has_key('username'):
        pid = request.session['username']
        Coursepost = CourseDetail.objects.filter(PId=pid)
        data = []
        for course in Coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)
        lastsubmission = Submission.objects.get(pk=subid)
        question = QuestionDetail.objects.get(pk=lastsubmission.QuestionId_id)
        assignment = AssignmentDetail.objects.get(pk=lastsubmission.AssignmentId_id)
        course = CourseDetail.objects.get(pk=assignment.Courseid_id)
        print(lastsubmission.StudentId_id)
        student = StudentDetail.objects.get(SId=lastsubmission.StudentId_id)
        all_submissions_of_question = Submission.objects.filter(QuestionId_id=lastsubmission.QuestionId_id,
                                                                StudentId_id=lastsubmission.StudentId_id).order_by(
            '-SubmissionTime')

        return render(request, 'professor/view_submissions.html', context={'assignment': assignment,
                                                                           'course': course,
                                                                           'question': question,
                                                                           'submissions': all_submissions_of_question,
                                                                           'student': student, 'data': data})
    return HttpResponse("Not Logged in")


def professor_login(request):
    username = "not logged in"

    if request.method == "POST":
        # Get the posted form
        professorLoginForm = ProfessorLoginForm(request.POST)

        if professorLoginForm.is_valid():
            username = professorLoginForm.cleaned_data['username']
            request.session['username'] = username
            s = ProfessorDetail.objects.filter(PId=username)
            if s.count() == 0:
                return HttpResponse("Enter valid username & password")
            if (s[0].Password != professorLoginForm.cleaned_data['password']):
                return HttpResponse("Enter valid username & password")

    else:
        professorLoginForm = ProfessorLoginForm()
        return render(request, 'professor/professor_login.html')
    return redirect('professor_home')


def professor_home(request):
    if request.session.has_key('username'):
        pid = request.session['username']
        Coursepost = CourseDetail.objects.filter(PId=pid)
        data = []
        for course in Coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)
        return render(request, 'professor/professor_home.html', {'Coursepost': Coursepost, 'data': data})
    return HttpResponse("Not Logged in")


def ProfessorFormView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'professor/professor_home.html', {"username": username})
    else:
        return render(request, 'professor/professor_login.html', {})


##############################################STUDENT IMPLEMENTATION#######################################################
def view_question_student(request, aid_qid):
    if request.session.has_key('username'):
        sid = request.session['username']
        Coursepost = CourseDetail.objects.filter(course_student__SId=sid)
        data = []
        for course in Coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)
        aid = aid_qid.split("_")[0]
        qid = aid_qid.split("_")[1]
        question = QuestionDetail.objects.get(pk=qid)
        assignment = AssignmentDetail.objects.get(pk=aid)
        course = CourseDetail.objects.get(id=1)
        professor = ProfessorDetail.objects.get(pk=course.PId_id)
        inpf1 = question.TestCaseInputFile1
        inpf1.open(mode='rb')
        inp1 = inpf1.read()
        inpf1.close()
        inpf2 = question.TestCaseInputFile2
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
        return render(request, 'student/view_question_student.html', context={'question': question,
                                                                              'assignment': assignment,
                                                                              'inp1': inp1, 'inp2': inp2,
                                                                              'out1': out1, 'out2': out2,
                                                                              'course': course, "professor": professor,
                                                                              "sid": sid,
                                                                              'data': data})
    return HttpResponse("Not Logged in")


def view_report_wise_student(request, aid):
    if request.session.has_key('username'):
        sid = request.session['username']
        Coursepost = CourseDetail.objects.filter(course_student__SId=sid)
        data = []
        for course in Coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)
        username = request.session['username']
        all_assignments_reports = []
        total_number_of_question = 0
        total_number_of_attempted_question = 0
        total_number_of_solved_question = 0
        assignments = AssignmentDetail.objects.filter(Courseid_id=AssignmentDetail.objects.get(id=aid).Courseid_id)
        for assignment in assignments:
            assignment_report = {}
            assignment_report['assignment'] = assignment
            assignment_report['no_of_attempted_question'] = 0
            assignment_report['no_of_solved_question'] = 0
            questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
            all_questions_report = []
            for question in questions:
                question_report = {}
                question_report['correct'] = False
                total_number_of_question += 1
                question_report['question'] = question
                submissions = Submission.objects.filter(QuestionId_id=question.id, StudentId_id=username).order_by(
                    '-SubmissionTime')
                question_report['no_of_submissions'] = submissions.count()
                if submissions.count() is not 0:
                    question_report['attempted'] = True
                    total_number_of_attempted_question += 1
                    assignment_report['no_of_attempted_question'] += 1
                    if submissions.first().Result == 'correct':
                        question_report['correct'] = True
                        total_number_of_solved_question += 1
                        assignment_report['no_of_solved_question'] += 1
                    question_report['subid'] = submissions.first().id
                else:
                    question_report['attempted'] = False
                all_questions_report.append(question_report)
            assignment_report['questions'] = all_questions_report
            all_assignments_reports.append(assignment_report)
        print(aid)
        return render(request, 'student/report_assignmentwise.html',
                      context={'all_assignments_report': all_assignments_reports,
                               'total_number_of_question': total_number_of_question,
                               'total_number_of_solved_question': total_number_of_solved_question,
                               'total_number_of_attempted_question': total_number_of_attempted_question,
                               'selected': aid, 'data': data})
    return HttpResponse("Not Logged in")


def view_report_student(request, cid):
    if request.session.has_key('username'):
        sid = request.session['username']
        Coursepost = CourseDetail.objects.filter(course_student__SId=sid)
        data = []
        for course in Coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)
        username = request.session['username']
        all_assignments_reports = []
        total_number_of_question = 0
        total_number_of_attempted_question = 0
        total_number_of_solved_question = 0
        assignments = AssignmentDetail.objects.filter(Courseid_id=cid)
        for assignment in assignments:
            assignment_report = {}
            assignment_report['assignment'] = assignment
            assignment_report['no_of_attempted_question'] = 0
            assignment_report['no_of_solved_question'] = 0
            questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
            all_questions_report = []
            for question in questions:
                question_report = {}
                question_report['correct'] = False
                total_number_of_question += 1
                question_report['question'] = question
                submissions = Submission.objects.filter(QuestionId_id=question.id,
                                                        StudentId_id=username).order_by('-SubmissionTime')
                question_report['no_of_submissions'] = submissions.count()
                if submissions.count() is not 0:
                    question_report['attempted'] = True
                    total_number_of_attempted_question += 1
                    assignment_report['no_of_attempted_question'] += 1
                    if submissions.first().Result == 'correct':
                        question_report['correct'] = True
                        total_number_of_solved_question += 1
                        assignment_report['no_of_solved_question'] += 1
                    question_report['subid'] = submissions.first().id
                else:
                    question_report['attempted'] = False
                all_questions_report.append(question_report)
            assignment_report['questions'] = all_questions_report
            all_assignments_reports.append(assignment_report)
        return render(request, 'student/report_assignmentwise.html',
                      context={'all_assignments_report': all_assignments_reports,
                               'total_number_of_question': total_number_of_question,
                               'total_number_of_solved_question': total_number_of_solved_question,
                               'total_number_of_attempted_question': total_number_of_attempted_question,
                               'data': data})
        return HttpResponse("Not Logged in")


def student_course(request, cid):
    if request.session.has_key('username'):
        sid = request.session['username']
        Coursepost = CourseDetail.objects.filter(course_student__SId=sid)
        data = []
        for course in Coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)
        course = CourseDetail.objects.filter(id=cid)
        professor = ProfessorDetail.objects.filter(PId=course[0].PId)
        assignmentlist = AssignmentDetail.objects.filter(Courseid=course[0].id)
        return render(request, 'student/student_course.html',
                      {'course': course[0], 'assignmentlist': assignmentlist,
                       'data': data,
                       'professor_name': professor[0].Name,})
    return HttpResponse("Not Logged in")


def student_register(request):
    context = RequestContext(request)
    if request.method == 'POST':
        sf = StudentForm(data=request.POST, prefix='student')
        if sf.is_valid():
            sf.save()
            return redirect('/')
    else:
        sf = StudentForm(prefix='student')
    return render(request, 'student/student_register.html', {'sf': sf}, context)


def Student_login(request):
    username = "not logged in"

    if request.method == "POST":
        studentLoginForm = StudentLoginForm(request.POST)

        if studentLoginForm.is_valid():
            username = studentLoginForm.cleaned_data['username']
            request.session['username'] = username
            s = StudentDetail.objects.filter(SId=username)
            if s.count() == 0:
                return HttpResponse("Enter valid username & password")
            if (s[0].Password != studentLoginForm.cleaned_data['password']):
                return HttpResponse("Enter valid username & password")

        return redirect('student_home')

    else:
        studentLoginForm = StudentLoginForm()
        return render(request, 'student/student_login.html')


def student_home(request):
    if request.session.has_key('username'):
        sid = request.session['username']
        Coursepost = CourseDetail.objects.filter(course_student__SId=sid)
        data = []
        for course in Coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)
        sid = request.session['username']
        courses = CourseDetail.objects.filter(course_student__SId_id=sid)
        Studentpost = StudentDetail.objects.filter(SId=sid)
        return render(request, 'student/student_home.html', context={'Studentpost': Studentpost,
                                                                     'courses': courses, 'data': data})
        return HttpResponse("Not Logged in")


def view_assignment_student(request, asid):
    if request.session.has_key('username'):
        sid = request.session['username']
        Coursepost = CourseDetail.objects.filter(course_student__SId=sid)
        data = []
        for course in Coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)
        assignment = AssignmentDetail.objects.get(pk=asid)
        professor = ProfessorDetail.objects.get(pk=CourseDetail.objects.get(pk=assignment.Courseid_id).PId_id)
        languages = Assignment_languages.objects.filter(AssignmentId=asid)
        questions = QuestionDetail.objects.filter(assignmentquestion__AId=asid)
        return render(request, 'student/viewassignmentstudent.html', context={'assignment': assignment,
                                                                              'professor': professor,
                                                                              'languages': languages,
                                                                              'questions': questions, 'data': data})
    return HttpResponse("Not Logged in")


def StudentFormView(request):
    if request.session.has_key('username'):
        if request.session.has_key('username'):
            username = request.session['username']
            return render(request, 'student/studentlist.html', {"username": username})
        else:
            return render(request, 'student/student_login.html', {})


def logout(request):
    if request.session.has_key('username'):
        try:
            del request.session['username']
        except:
            pass
        return redirect('/')


def studentlist(request):
    if request.session.has_key('username'):
        studentposts = StudentDetail.objects.all()
        return render(request, 'student/studentlist.html', {'list': studentposts})
    return HttpResponse("Not Logged in")


def run_code(request):
    if request.session.has_key('username'):
        sid = request.session['username']
        Coursepost = CourseDetail.objects.filter(course_student__SId=sid)
        data = []
        for course in Coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)
        data = request.POST
        print(str(data))
        aid = data.get('asid')
        qid = data.get('qid')
        question = QuestionDetail.objects.get(pk=qid)
        assignment = AssignmentDetail.objects.get(pk=aid)
        course = CourseDetail.objects.get(id=1)
        professor = ProfessorDetail.objects.get(pk=course.PId_id)
        inpf1 = question.TestCaseInputFile1
        inpf1.open(mode='rb')
        inp1 = inpf1.read()
        inpf1.close()
        inpf2 = question.TestCaseInputFile2
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
        return render(request, 'student/view_question_student_result.html', context={'question': question,
                                                                                     'assignment': assignment,
                                                                                     'inp1': inp1, 'inp2': inp2,
                                                                                     'out1': out1, 'out2': out2,
                                                                                     'course': course,
                                                                                     "professor": professor,
                                                                                     "sid": sid, 'data': data})
        # if request.method == "POST":
        #     data=request.POST
        #     print(str(data))
        #     print(data.get('qid'))
        #     print(data.get('asid'))
        #     if data.get('lang')=='C':
        #         fo = open("media/code/temp-code.c", "wb")
        #         fo.write( bytes(data.get('source-code'),encoding="utf-8"))
        #         fo.close()
        #     elif data.get('lang')=='C++':
        #         fo = open("media/code/temp-code.cpp", "wb")
        #         fo.write( bytes(data.get('source-code'),encoding="utf-8"))
        #         fo.close()

        # Close opend file

        from subprocess import call
        # call(,shell=True)
        return render(request, 'student/view_question_student_result.html')


##############################################ASSISTANT IMPLEMENTATION#######################################################



def assistantlist(request):
    assistantposts = AssistantDetail.objects.all()
    return render(request, 'assistant/assistantlist.html', {' assistantposts': assistantposts})


def Assistant_login(request):
    username = "not logged in"
    if request.method == "POST":
        assistantLoginForm = AssistantLoginForm(request.POST)
        if assistantLoginForm.is_valid():
            username = assistantLoginForm.cleaned_data['username']
            request.session['username'] = username
            taid = AssistantDetail.objects.filter(TaId=username)
            if taid.count() == 0:
                return HttpResponse("Enter valid username & password")
            if (taid[0].Password != assistantLoginForm.cleaned_data['password']):
                return HttpResponse("Enter valid username & password")
            else:
                return HttpResponseRedirect('assistant_home')
    else:
        assistantLoginForm = AssistantLoginForm()
        return render(request, 'assistant/assistant_login.html')
        # return render(request, 'assistant/assistant_home.html', {'Course': coursepost})


def assistant_home(request):
    if request.session.has_key('username'):
        taid = request.session['username']
        post = Courses_Ta.objects.get(TaId_id=taid)
        coursepost = CourseDetail.objects.get(id=post.CourseId_id)
        data = []
        for course in coursepost:
            course_dict = {}
            course_dict['name'] = course.CourseName
            course_dict['id'] = course.id
            assignments = AssignmentDetail.objects.filter(Courseid_id=course.id)
            course_dict['assignments'] = []
            for assignment in assignments:
                assignment_dict = {}
                assignment_dict['name'] = assignment.AssignmentName
                assignment_dict['id'] = assignment.id
                questions = QuestionDetail.objects.filter(assignmentquestion__AId=assignment.id)
                assignment_dict['questions'] = []
                for question in questions:
                    question_dict = {}
                    question_dict['name'] = question.QName
                    question_dict['id'] = question.id
                    assignment_dict['questions'].append(question_dict)
                course_dict['assignments'].append(assignment_dict)
            data.append(course_dict)

        assistant = AssistantDetail.objects.filter(courses_ta__CourseId=post.CourseId_id)
        assignmentlist = AssignmentDetail.objects.all()
        studentlist = StudentDetail.objects.filter(course_student__CourseId=coursepost.id)
        talist = AssistantDetail.objects.filter(courses_ta__CourseId=coursepost.id)
        return render(request, 'assistant/assistant_home.html',
                      {'Course': coursepost, 'assignmentlist': assignmentlist,
                       'talist': talist, 'assistant': assistant, 'studentlist': studentlist,'data':data})
    return HttpResponse("Not Logged in")

############################################################################################################################
