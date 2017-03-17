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
    if request.method == "POST":
        form = PortfolioForm(request.POST or None, Portfolio)
        if form.is_valid():
            #portfolio = Portfolio
            #portfolio.user = User.objects.get(pk=request.session['user_id'])
            #portfolio.technical_tag = form.cleaned_data['technical_tag']
            return HttpResponseRedirect('partner/main')
        else:
            messages.error(request, 'error')
    return render(request, 'gamelancer_main/partner_portfolio_upload.html', {'form': PortfolioForm()})

@login_required(login_url='/accounts/login/')
def partner_portfolio(request):
    return render(request, 'gamelancer_main/partner_portfolio.html')