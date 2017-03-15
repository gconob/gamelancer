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
            return HttpResponseRedirect('/client/main')
    else:
        form = ProjectRegisterForm()
    return render(request, 'gamelancer_main/client_project_register.html', {'form': form})


@login_required(login_url='/accounts/login/')
def project_main(request):
    projects = dict()
    projects['projects'] = Project.objects.filter(client=request.session['user_id']).order_by('-closing_date')
    return render(request, 'gamelancer_main/client_project_main.html', projects)


@login_required(login_url='/accounts/login/')
def client_main(request):
    return render(request, 'gamelancer_main/client_main.html')