import re
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from . import models

class RegistrationForm(forms.Form):
    username = forms.CharField(label='id', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='password(Again)', widget=forms.PasswordInput())
    IS_CLIENT =[(0, 'client'), (1, 'partner')]
    usertype =  forms.ChoiceField(choices=IS_CLIENT, label='client or partner', widget=forms.RadioSelect())
    
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1=self.cleaned_data['password1']
            password2=self.cleaned_data['password2']
            if password1 == password2:
                return password2
        
        raise forms.ValidationError('패스워드가 일치하지 않습니다')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError('Username contains only alphanumeric characters and underscore')
        
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('username is already taken')      
    

class ProjectRegisterForm(forms.Form):
