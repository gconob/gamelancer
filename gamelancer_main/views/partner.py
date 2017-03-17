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
def partner_main(request):
    return render(request, 'gamelancer_main/partner_main.html')

@login_required(login_url='/accounts/login/')
def partner_user_page(request):
    return render(request, 'gamelancer_main/partner_user_page.html')

@login_required(login_url='/accounts/login/')
def partner_portfolio_upload(request):
    form = PortfolioForm()
    return render(request, 'gamelancer_main/partner_portfolio_upload.html', {'form':form})

@login_required(login_url='/accounts/login/')
def partner_portfolio(request):
    return render(request, 'gamelancer_main/partner_portfolio.html')