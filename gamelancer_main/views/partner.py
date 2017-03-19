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

#pos key : U01TX0FVVEgyMDE3MDMxMjAyMTcxNTE5NTk4
import pdb



@login_required(login_url='/accounts/login/')
def partner_main(request):
    return render(request, 'gamelancer_main/partner_main.html')

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
        args['form'] = form
    return render(request, 'gamelancer_main/partner_project_apply.html', args)


#프로젝트 상세화면
@login_required(login_url='/accounts/login')
def partner_portfolio_detail(request, id):
    portfolio = Portfolio.objects.get(id=id)
    technical_tag = portfolio.technical_tag.split(',')
    context = {"portfolio" : portfolio,'technical_tag':technical_tag }
    return render(request, 'gamelancer_main/partner_portfolio_detail.html', context)