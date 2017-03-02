from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

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
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')
    
def loggedin(request):
    return render_to_response('gamelancer_main/client_main.html', {'username':request.user.username})

def invalid_login(request):
    return render_to_response('gamelancer_main/index.html')

def logout(request):
    return render_to_response('gamelancer_main/index.html')

def client_main(request):
    return render(request, 'gamelancer_main/main_client.html')

def partner_main(request):
    return render(request, 'gamelancer_main/main_parter.html')

