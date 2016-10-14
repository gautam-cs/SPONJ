__author__ = 'Gautam'


from PROFESSOR.models import QuestionDetail
from PROFESSOR.forms import QuestionForm
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.contrib import auth
from django.conf import settings


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

"""def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        upf = UserProfileForm(request.POST, prefix='userprofile')
        if uf.is_valid() * upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return HttpResponseRedirect(index.html)
    else:
        uf = UserForm(prefix='user')
        upf = UserProfileForm(prefix='userprofile')
    return django.shortcuts.render_to_response('register.html',
                                               dict(userform=uf,
                                                    userprofileform=upf),
                                               context_instance=django.template.RequestContext(request))

"""

