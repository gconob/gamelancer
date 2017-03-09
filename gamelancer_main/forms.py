import re
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm
from gamelancer_main.models import *
from gamelancer_main.category import *

class Html5Date(forms.DateInput):
    input_type = 'date'
    
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
    
'''
class ProjectRegisterForm(ModelForm):
    class Meta:
        model = Project 
        fields = ['title', 'desc' ]#, 'technical_tag', 'duration', 'register_time', 'work_start_date', 'closing_date', 'budget')
'''        

class ProjectRegisterForm(forms.Form):
    title = forms.CharField(label='제목 ', max_length=140)
    desc = forms.CharField(label='상세설명 ', widget=forms.Textarea)
    duration = forms.IntegerField(label="예상기간 ")
    technical_tag1 = forms.CharField(label="기술태그" , max_length=32)
    technical_tag2 = forms.CharField(label="기술태그" , max_length=32)
    technical_tag3 = forms.CharField(label="기술태그" , max_length=32)
    technical_tag4 = forms.CharField(label="기술태그" , max_length=32)
    technical_tag5 = forms.CharField(label="기술태그" , max_length=32)
    work_start_date = forms.DateTimeField(label="예상업무시작일 ", widget=Html5Date)
    closing_date = forms.DateField(label="마감일", widget=Html5Date)
    budget = forms.IntegerField(label="예산") 
    category1 = forms.ChoiceField(choices=FUNCTIONAL_CATEGORY, label="기능별 ", initial='', widget=forms.Select())
    category2 = forms.ChoiceField(choices=TECHNICAL_CATEGORY, label="기술별 ", initial='', widget=forms.Select())
    category3 = forms.ChoiceField(choices=PLATFORM_CATEGORY, label="플랫폼별 ", initial='', widget=forms.Select())
    category4 = forms.ChoiceField(choices=GENRE_CATEGORY, label="장르별 ", initial='', widget=forms.Select())
    
    
            
        
    '''
    def __init__(self, *args, **kwargs):
        super(ProjectRegisterForm, self).__init__(*args, **kwargs)
        category = ProjectCategory_Master.objects.all()
        root = []
        for i in category:
            if i.parent_id == 0:
                root.append(i)
                
        for x in root:
            self.fields[x.title] = forms.CharField(label=x.title)
            for y in category:
                if y.parent_id == x.id:
                    self.fields['category_%d' %  y.id] = forms.BooleanField(label=y.title)
   ''' 