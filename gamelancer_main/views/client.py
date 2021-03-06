from django.shortcuts import render
from django.http import Http404
from django.template import RequestContext
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
    apply['ProjectApply'] = ProjectApply.objects.filter(project = Project.objects.filter(client=request.user))
    return render(request, "gamelancer_main/client_apply_manage.html", apply)


#============================
# 프로젝트 등록
#============================
@login_required(login_url='/accounts/login/')
def project_register(request):
    if request.method == 'POST':
        form = ProjectRegisterForm(request.POST)

        if form.is_valid():
            project = Project()
            project.client = User.objects.get(pk=request.session['user_id'])
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
            privatenotice = PrivateNotice()
            privatenotice.type = 1
            privatenotice.project = project
            privatenotice.desc = '프로젝트 등록'
            privatenotice.reader = request.user
            privatenotice.actor = request.user
            privatenotice.save()
            return HttpResponseRedirect('/client/main')
    else:
        form = ProjectRegisterForm()
    return render(request, 'gamelancer_main/client_project_register.html', {'form': form})


@login_required(login_url='/accounts/login/')
def project_main(request):
    context = dict()
    try:
        context['projects'] = Project.objects.filter(client=request.session['user_id']).order_by('-closing_date')
        context['profile'] = Profile.objects.get(user_id=request.session['user_id']);
        context['user'] = Profile.objects.get(pk = request.session['user_id'])
    except ObjectDoesNotExist:
        context['projects'] = None
    return render(request, 'gamelancer_main/client_project_main.html', context)


@login_required(login_url='/accounts/login/')
def client_main(request):
    return render(request, 'gamelancer_main/client_main.html')






'''
=== 클라이언트 자기 정보 관리 =====

'''
#=====================
# 클라이언트 자기소개
#=====================
@login_required(login_url='/accounts/login/')
def client_user(request):
    context = dict()
    profile = Profile.objects.get(user=request.user)
    context['profile'] = profile

    if request.method == 'POST':
        form = ClientIntroForm(request.POST)
        if form.is_valid():
            requesttype = request.POST.get('requesttype')
            profile = Profile.objects.get(user_id=request.user.id)
            if requesttype=='desc':
                profile.desc = request.POST.get('desc')
                profile.save()
            if requesttype=='address':
                profile.address1 = request.POST.get('address1')
                profile.address2 = request.POST.get('address2')
                profile.save()

            context['msg'] = '저장하였습니다'
            context['form'] = form
            return render(request, 'gamelancer_main/client_userinfo.html', context)

    context['form'] = ClientIntroForm()
    return render(request, 'gamelancer_main/client_userinfo.html', context)

# =================
# 패스워드 변경
# =================
# 패스워드 편경하기 전에 확인차 패스워드를 한 번 더 물어 본다.
def client_password_change(request):
    context = dict()
    if request.POST:
        doctype = request.POST.get("doctype")
        if doctype == "verify":
            username = request.user.username
            password = request.POST.get('password')

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    context['type'] = 'passwordchange'
                    context['form'] = PasswordChangeForm()
                    return render(request, 'gamelancer_main/client_password_change.html', context)

            context['msg'] = '패스워드가 일치하지 않습니다'
            context['type'] = 'passwordprechange'
            return render(request, 'gamelancer_main/client_password_change.html', context)

        if doctype == "passwordchange":
            form = PasswordChangeForm(request.POST)
            if form.is_valid():
                u = User.objects.get(pk=request.session['user_id'])
                u.set_password(request.POST.get('password1'))
                u.save()
                context['msg'] = '패스워드가 변경되었습니다'
                return render(request, 'gamelancer_main/client_main.html', context)
            else:
                context['type'] = "passwordchange"
                context['form'] = form
                return render(request, 'gamelancer_main/client_password_change.html', context)

    context['type'] = 'passwordprechange'
    return render(request, 'gamelancer_main/client_password_change.html', context)

#==============================
# 계좌 관리
#==============================
def client_account(request):
    context = dict()
    if request.POST:
        form = ClientAccountForm(request.POST)
        if form.is_valid():
            profile = Profile.objects.get(user_id=request.user.id)
            profile.account_bank = request.POST.get('bank_name')
            profile.account_number = request.POST.get('account_number')
            profile.account_owner_name = request.POST.get('account_owner')
            profile.save()
            context['msg'] = '계좌정보를 변경하였습니다'
        else:
            context['msg'] = '계좌정보를 변경할 수 없습니다'
    else:
        form = ClientAccountForm()
    context['form'] = form
    return render(request, 'gamelancer_main/client_account.html', context)


#=============================
# 신원인증
#=============================
def client_verify(request):
    context= dict()
    if request.POST:
        form = ClientAuthForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            context['msg'] = '저장하였습니다'
    else:
        form = ClientAuthForm()
    context['form'] = form
    return render(request, 'gamelancer_main/client_verify.html', context)

