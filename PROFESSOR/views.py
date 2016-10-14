__author__ = 'Gautam'


from PROFESSOR.models import QuestionDetail
from PROFESSOR.forms import QuestionForm,UserForm
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import redirect
from django.contrib import auth
from django.conf import settings
from django.shortcuts import render, get_object_or_404,render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf



def login(request):
    next = request.POST.get('next', 'index/')
    if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)


            if user is not None:
                    if user.is_active:
                            auth.login(request, user)

                            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
                    else:
                            return HttpResponse("Inactive user.")
            else:
                    return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

#@login_required(redirect_field_name='next')
def index(request):
    return render (request, "index.html")


def question(request):
    return render(request,'question.html')

def question(request):
    if request.method=="POST":
        form=QuestionForm(request.POST)
        if form.is_valid():
            Post=form.save()
            return redirect('qbank')
    else:
        form=QuestionForm()
    return render(request,'question.html',{'form':form})

def qbank(request):
	QuestionPosts=QuestionDetail.objects.all()
	return render(request, 'qbank.html', {'QuestionPosts':QuestionPosts})


def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_admin = True
            user.is_staff = True
            user.is_superuser = True
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render_to_response('register.html',
            {'user_form': user_form,'registered': registered},context)