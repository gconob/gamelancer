from django.shortcuts import render
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from gamelancer_main.forms import *
from django.contrib.auth.decorators import login_required
from ..models import Profile
from django.utils.datastructures import MultiValueDictKeyError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from gamelancer_main import category



import pdb



@login_required(login_url='/accounts/login/')
def partner_main(request):

    if request.method == 'POST':
        #form = ProjectSearchForm(request.POST)
        project_desc = str(request.POST['project_desc'])
        try:
            project_sort = str(request.POST['project_sort'])
        except MultiValueDictKeyError:
            project_sort = ""

        if (len(project_desc) != 0 and len(project_sort) != 0):
            projects = Project.objects.filter(desc__contains=project_desc).order_by(project_sort)
        elif len(project_desc) != 0 and len(project_sort) == 0:
            projects = Project.objects.filter(desc__contains=project_desc)
        elif (len(project_desc) == 0 and len(project_sort) != 0):
            projects = Project.objects.order_by(project_sort)
        else:
            projects = Project.objects.all()
    else:
        projects = Project.objects.all()

    paginator = Paginator(projects, 1)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'gamelancer_main/partner_main.html', {'projects':contacts, 'category' : category})

@login_required(login_url='/accounts/login/')
def partner_manage(request):

    if request.method == 'POST':
        #form = ProjectSearchForm(request.POST)
        try:
            project_sort = str(request.POST['project_sort'])
        except MultiValueDictKeyError:
            project_sort = ""

        if (len(project_sort) != 0):
            projects = Project.objects.order_by(project_sort)
        else:
            projects = Project.objects.all()
    else:
        projects = Project.objects.all()

    paginator = Paginator(projects, 10)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'gamelancer_main/partner_manage.html', {'projects':contacts})


@login_required(login_url='/accounts/login/')
def partner_user_page(request):
    return render(request, 'gamelancer_main/partner_user_page.html')

@login_required(login_url='/accounts/login/')
def partner_portfolio_upload(request):
    args = {}
    if request.method == "POST":
        #form = PortfolioForm(request.POST or None, PortfolioForm)
        form = PortfolioForm(request.POST, request.FILES, user=request.user)
        user = User.objects.get(pk=request.session['user_id'])
        if form.is_valid():
            port = form.save(commit=False)
            port.user = user
            port.save()
            #portfolio = Portfolio
            #portfolio.user = User.objects.get(pk=request.session['user_id'])
            #portfolio.technical_tag = form.cleaned_data['technical_tag']
            return HttpResponseRedirect('/partner/main')
    else:
        form = PortfolioForm()
    args['form'] =form
    return render(request, 'gamelancer_main/partner_portfolio_upload.html', args)

@login_required(login_url='/accounts/login/')
def partner_portfolio(request):
    portfolios = Portfolio.objects.filter(user=request.user)
    #portfolios = Portfolio.objects.all()
    context = {"portfolios":portfolios}
    return render(request, 'gamelancer_main/partner_portfolio.html', context)

@login_required(login_url='/accounts/login/')
def partner_project_apply(request, id):
    args = {}
    if request.method == "POST":
        form = ProjectApplyForm(request.POST)

        user = User.objects.get(pk=request.session['user_id'])
        project = Project.objects.get(id=id)
        if form.is_valid():
            apply = form.save(commit=False)
            apply.user = user
            apply.project = project
            apply.save()
            return HttpResponseRedirect('/partner/main')
    else:
        form = ProjectApplyForm()
        form.fields['portfolio1'].queryset = Portfolio.objects.filter(user=request.user)
        form.fields['portfolio2'].queryset = Portfolio.objects.filter(user=request.user)
        form.fields['portfolio3'].queryset = Portfolio.objects.filter(user=request.user)
        args['form'] = form
    return render(request, 'gamelancer_main/partner_project_apply.html', args)


#프로젝트 상세화면
@login_required(login_url='/accounts/login')
def partner_portfolio_detail(request, id):
    portfolio = Portfolio.objects.get(id=id)
    technical_tag = portfolio.technical_tag.split(',')
    context = {"portfolio" : portfolio,'technical_tag':technical_tag }
    return render(request, 'gamelancer_main/partner_portfolio_detail.html', context)

#경력, 학력, 자격증, 기술
@login_required(login_url='/accounts/login')
def partner_resume(request):
    '''
    if request.method == "POST":
        save_or_delete = 0
        if 'add_technique' in request.POST:
            form = TechniqueForm(Request.POST)
            save_or_delete = 1
        if 'add_education' in request.POST:
            form = EducationForm(Request.POST)
            save_or_delete = 1
        if 'add_workhistory' in request.POST:
            form = WorkHistoryForm(Request.POST)
            save_or_delete = 1
        if 'add_license' in request.POST:
            form = LicenseForm(Request.POST)
            save_or_delete = 1

        if save_or_delete == 1:
            save_form = form.save(commit = false)
            save_form.user = request.user
            #save_form.user = User.objects.get(pk=request.session['user_id'']
            save_form.save()


        if 'delete_technique' in request.POST:
            id = request.POST.get('technique_id')
            PartnerTechnic.objects.get(id = id).delete()

        if 'delete_education' in request.POST:
            id = request.POST.get('education_id')
            PartnerEducation.objects.get(id = id).delete()

        if 'delete_workhistory' in request.POST:
            id = request.POST.get('workhistory_id')
            PartnerWorkHistory.objects.get(id = id).delete()

        if 'delete_license' in request.POST:
            id = request.POST.get('license_id')
            PartnerLicense.objects.get(id = id).delete()
    else:
    '''
    context = {}
    education  = PartnerEducation.objects.filter(user=request.user)
    context['education'] = education
    context['license'] = PartnerLicense.objects.filter(user=request.user)
    context['technique'] = PartnerTechnic.objects.filter(user=request.user)
    context['workhistory'] = PartnerWorkHistory.objects.filter(user=request.user)

    return render(request, 'gamelancer_main/partner_resume.html', context)


#자기 소개
def partner_desc(request):
    profile = Profile.objects.get(user_id = request.user.id)
    return render(request, 'gamelancer_main/partner_desc.html', {'profile':profile })