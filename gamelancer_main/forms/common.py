import re

from django import forms
from django.core.exceptions import ObjectDoesNotExist
from gamelancer_main.models import *
from gamelancer_main.category import *



class RegistrationForm(forms.Form):
    username = forms.CharField(label='id', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='password(Again)', widget=forms.PasswordInput())
    usertype = forms.ChoiceField(choices=USER_TYPE, label='파트너 혹은 클라이언트를 선택하세요', widget=forms.RadioSelect())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2

        raise forms.ValidationError('패스워드가 일치하지 않습니다')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username contains only alphanumeric characters and underscore')

        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('username is already taken')
