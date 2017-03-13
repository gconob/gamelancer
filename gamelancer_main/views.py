from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from gamelancer_main.forms import *
from django.contrib.auth.decorators import login_required
from .models import UserProfile

#pos key : U01TX0FVVEgyMDE3MDMxMjAyMTcxNTE5NTk4 
import pdb

def index(request):
    return render(request, 'gamelancer_main/index.html')

def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('gamelancer_main/login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth.login(request, user)            
            userprofile = UserProfile(user=user)
            request.session['user_id']=user.id
            request.session['user_name']=user.username
            if (userprofile.usertype  == '0') or (userprofile.usertype == 0):
                return HttpResponseRedirect('/client/main')
            if (userprofile.usertype == '1') or (userprofile.usertype== 1):
                return HttpResponseRedirect('/partner/main')    
  #  c={}
  #  c.update(csrf(request))
  #  return render_to_response('gamelancer_main/login.html', c)
    return login(request)
        

@login_required(login_url='/accounts/login/')
def client_main(request):
    return render(request, 'gamelancer_main/client_main.html')

@login_required(login_url='/accounts/login/')
def partner_main(request):
    return render(request, 'gamelancer_main/parter_main.html')

def register(request):  
    if request.method=='POST':
        form = RegistrationForm(request.POST)
       
        if form.is_valid():            
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password1'], email=form.cleaned_data['email'])
            userprofile = UserProfile(user=user, usertype = form.cleaned_data['usertype'])
            userprofile.save()
            request.session['user_id'] = user.id; 
            request.session['user_name'] =user.username
            if userprofile.usertype == '0':
                return render(request, 'gamelancer_main/client_main.html')
                #return HttpResponseRedirect('/client/main')            
            elif userprofile.usertype =='1':
                return render(request, 'gamelancer_main/partner_main.html')
                #return HttpResponseRedirect('/partner/main')
            else:
                return render(request, 'gamelancer_main/client_main.html', {'usertype':userprofile.usertype})
    else:                   
        form = RegistrationForm( initial={'usertype':0})
    
    return render(request, 'gamelancer_main/register.html', {'form':form})
 
@login_required(login_url='/accounts/login/')
def project_register(request):
    if request.method=='POST':
        form = ProjectRegisterForm(request.POST)
        
        if form.is_valid():
            project = Project()
            project.client = User.objects.get(pk = request.session['user_id'])
            project.title = form.cleaned_data['title']
            project.desc = form.cleaned_data['desc']
            project.duration = form.cleaned_data['duration']
            project.technical_tag = form.cleaned_data['technical_tag']
            project.work_start_date = form.cleaned_data['work_start_date']
            project.closing_date = form.cleaned_data['closing_date']
            project.budget = form.cleaned_data['budget']
            project.category1 = form.cleaned_data['category1']
            project.category2 = form.cleaned_data['category2']
            project.category3 = form.cleaned_data['category3']                        
            project.save()
            return HttpResponseRedirect('/client/main')        
    else:    
        form = ProjectRegisterForm()
    return render(request, 'gamelancer_main/client_project_register.html', {'form':form })

@login_required(login_url='/accounts/login/')    
def project_main(request):
    projects = dict()
    projects['projects'] = Project.objects.filter(client=request.session['user_id']).order_by('-closing_date') 
    return render(request, 'gamelancer_main/client_project_main.html', projects)   

@login_required(login_url='/accounts/login/')
def project_detail(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("프로젝트를 찾을 수 없습니다")
    return render(request, "gamelancer_main/client_project_detail.html", {'project_id': project_id})
  
@login_required(login_url='/accounts/login/')
def client_apply_manage(request):
    apply = dict()
    apply['ProjectApply'] = ProjectApply.objects.filter()
    return render(request, "gamelancer_main/client_apply_manage.html")
