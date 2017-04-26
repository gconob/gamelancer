from django.shortcuts import render
from django.http import HttpResponseRedirect
from gamelancer_main.forms import *
from django.contrib.auth.decorators import login_required
from ..models import Profile
from django.utils.datastructures import MultiValueDictKeyError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from gamelancer_main import category
from django.db.models import Q
from functools import reduce
import operator
import pdb
import datetime


@login_required(login_url='/accounts/login/')
def partner_main(request):

    program_selected_values = []

    if request.method == 'POST':
        form = ProjectSearchForm(request.POST)
        #project_desc = str(request.POST['project_desc'])    # TODO
        project_sort = request.POST.get('project_sort', '') # TODO

        combine_filter = Project.objects.all()

        desc = str(form['desc'].value())
        if (len(desc) > 0):
            combine_filter = combine_filter.filter(desc__contains=desc)

        category1 = str(form['category1'].value())
        print("category1:"+category1)
        if (len(category1) > 0):
            combine_filter = combine_filter.filter(category1=category1)

        category2 = str(form['category2'].value())
        print("category2:" + category2)
        if (len(category2) > 0):
            combine_filter = combine_filter.filter(category2=category2)

        category3 = str(form['category3'].value())
        print("category3:" + category3)
        if (len(category3) > 0):
            combine_filter = combine_filter.filter(category3=category3)

        #project_sort = str(form['project_sort'].value())
        if (len(project_sort) > 0):
            combine_filter = combine_filter.order_by(project_sort)

        program_selected_values = request.POST.getlist('program') # TODO
        #print(program_selected_values)
        list_of_Q = [Q(**{'technical_tag__contains': val}) for val in program_selected_values]
        if (len(list_of_Q) > 0):
            combine_filter = combine_filter.filter(reduce(operator.or_, list_of_Q))

        #print(combine_filter)
        projects = combine_filter

    else:
        form = ProjectSearchForm()
        projects = Project.objects.all()

    paginator = Paginator(projects, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'gamelancer_main/partner_main.html', {'projects':contacts, 'category' : category, 'form' : form, 'programList' : program_selected_values})

@login_required(login_url='/accounts/login/')
def partner_manage(request):

    if request.method == 'POST':
        #form = ProjectRegisterForm(request.POST)
        project_sort = request.POST.get('project_sort', '')

        if (len(project_sort) > 0):
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
            notice = PrivateNotice()
            notice.user = project.client
            notice.title = '프로젝트 지원 알림'
            notice.desc = project.partner + '님께서 ' + project.title + '에 지원하셨습니다'
            notice.notice_time = str(datetime.datetime.now())

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