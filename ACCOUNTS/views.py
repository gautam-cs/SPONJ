__author__ = 'Gautam'


from ACCOUNTS.models import QuestionDetail,ProfessorDetail
from ACCOUNTS.forms import QuestionForm,UserForm,UserProfileForm
from django.conf import settings
from django.shortcuts import render, get_object_or_404,render_to_response
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from itertools import chain


def index(request):
    return render (request, "index.html")



def user_login(request):
    context = RequestContext(request)
    Users=User.objects.all()
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print("auth",str(authenticate(username=username, password=password)))

        if user:
        # Is the account active? It could have been disabled.
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index')
            else:
                return HttpResponse("/index")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("please choose your valid username & password: {0}, {1}".format(username, password))
            return HttpResponse("please choose your valid username & password ")
    else:
        return render_to_response('professor/plogin.html', {}, context)



def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

#@login_required(redirect_field_name='next')



def question(request):
    if request.method=="POST":
        form=QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('qbank')
    else:
        form=QuestionForm()
    return render(request,'question\question.html',{'form':form})

def qbank(request):
	QuestionPosts=QuestionDetail.objects.all()
	return render(request, 'question\qbank.html',{'QuestionPosts':QuestionPosts})


def pregister(request):
    context = RequestContext(request)
    if request.method == 'POST':
        uf = UserForm(data=request.POST, prefix='user')
        upf = UserProfileForm(data=request.POST, prefix='userprofile')
        if uf.is_valid() * upf.is_valid():
            user=uf.save()
            userprofile=upf.save(commit=False)
            userprofile.user=user
            userprofile.save()
            return redirect('professorlist')
    else:
        uf=UserForm(prefix='user')
        upf = UserProfileForm(prefix='userprofile')
    return render(request,'professor\pregister.html', {'uf':uf,'upf':upf}, context)

def professorlist(request):
    professorposts = ProfessorDetail.objects.all()
    userposts=User.objects.all()
    list = chain(professorposts,userposts)
    return render(request, 'professor\professorlist.html',{'list':list})
