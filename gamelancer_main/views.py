from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from gamelancer_main.forms import *
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
            return HttpResponseRedirect('/accounts/loggedin')
            
    return HttpResponseRedirect('/accounts/invalid')
      
def loggedin(request):
    return render_to_response('gamelancer_main/client_main.html', {'username':request.user.username})

def invalid_login(request):
    return render_to_response('gamelancer_main/index.html')

def logout(request):
    return render_to_response('gamelancer_main/index.html')

def client_main(request):
    return render(request, 'gamelancer_main/client_main.html')

def partner_main(request):
    return render(request, 'gamelancer_main/parter_main.html')

def register(request):
   # pdb.set_trace()
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            #pdb.set_trace()
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password1'], email=form.cleaned_data['email'])
            return HttpResponseRedirect('/client/main')
            #return render_to_response('gamelancer_main/main_client.html')
    form = RegistrationForm()
 #   variables = RequestContext(request, {'form': form})
    return render(request, 'gamelancer_main/register.html', {'form':form})
    #return render_to_response(request, 'gamelancer_main/register.html')
