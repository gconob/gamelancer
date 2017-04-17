from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from gamelancer_main.forms import *
from django.contrib.auth.decorators import login_required
from ..models import Profile

#pos key : U01TX0FVVEgyMDE3MDMxMjAyMTcxNTE5NTk4
import pdb



def index(request):
    return render(request, 'gamelancer_main/index.html')


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('gamelancer_main/login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            usertype = user.profile.usertype;
            request.session['user_id'] = user.id
            request.session['user_name'] = user.username
            request.session['user_type'] = usertype
            if usertype == 0:
                return HttpResponseRedirect('/client/main')
            if usertype == 1:
                return HttpResponseRedirect('/partner/main')

                #  c={}
                #  c.update(csrf(request))
                #  return render_to_response('gamelancer_main/login.html', c)
    return login(request)

#====================================
# 회원가입
#====================================

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password1'], email=form.cleaned_data['email'])
            userprofile = Profile(user=user, usertype=form.cleaned_data['usertype'])
            userprofile.save()
            request.session['user_id'] = user.id;
            request.session['user_name'] = user.username
            if userprofile.usertype == '0':
                return render(request, 'gamelancer_main/client_main.html')
                # return HttpResponseRedirect('/client/main')
            elif userprofile.usertype == '1':
                return render(request, 'gamelancer_main/partner_main.html')
                # return HttpResponseRedirect('/partner/main')
            else:
                return render(request, 'gamelancer_main/client_main.html', {'usertype': userprofile.usertype})
    else:
        form = RegistrationForm(initial={'usertype': 0})

    return render(request, 'gamelancer_main/register.html', {'form': form})


#==================================
# 이용방법
#==================================

def howtouse_main(request):
    return render(request, 'gamelancer_main/howtouse_main.html')

def howotuse_client(request):
    return render(request, 'gamelancer_main/howtouse_client.html')

def howtouse_partner(request):
    return render(request, 'gamelancer_main/howtouse_partner.html')

def howtouse_faq(request):
    return render(request, 'gamelancer_main/howtouse_faq.html')

def howtouse_fare(request):
    return render(request, 'gamelancer_main/howtouse_fare.html')

#=====================
# 이용약관
#=====================
def terms_of_service(request):
    return render(request, 'gamelancer_main/terms_of_service.html')

#=====================
# 메시지
#======================
def message(request):
    context = dict()
    context['notices']= PrivateNotice.objects.filter(reader=request.user).order_by('-id')
    PrivateNotice.objects.filter(reader=request.user).update(readyn = True)
    return render(request, 'gamelancer_main/message.html', context)
