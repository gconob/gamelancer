from django import forms
from django.forms import  ModelForm, Textarea
from gamelancer_main.models import *
from .html5 import Html5Date
from gamelancer_main.category import *

class PortfolioForm(forms.ModelForm):
    category1 = forms.ChoiceField(choices=FUNCTIONAL_CATEGORY, label="기능별 ", initial='', widget=forms.Select())
    category2 = forms.ChoiceField(choices=PLATFORM_CATEGORY, label="플랫폼별 ", initial='', widget=forms.Select())
    category3 = forms.ChoiceField(choices=GENRE_CATEGORY, label="장르별 ", initial='', widget=forms.Select())

    class Meta:
        model = Portfolio
#        fields = ['title', 'desc', 'start_day', 'end_day', 'image1','image2']
        exclude = ['user','category1', 'category2', 'category3', ]
        widgets = {'desc': Textarea(attrs={'cols':80, 'rows':10}), 'start_day' : Html5Date, 'end_day':Html5Date, }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', '')
        super(PortfolioForm, self).__init__(*args, **kwargs)

    def clean_technical_tag(self):
        if 'technical_tag' in self.cleaned_data:
            technical_tag = self.cleaned_data['technical_tag']
            tags = technical_tag.split()
            if len(tags) > 5 :
                raise forms.ValidationError("기술 태그는 최대 5개까지 적을 수 있습니다")
        return technical_tag


class ProjectApplyForm(forms.ModelForm):
    class Meta:
        model = ProjectApply
        exclude=['user','project']
'''
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(ProjectApplyForm, self).__init__(**kwargs)
        if user:
            self.fields['portfolio1'].queryset = Portfolio.objects.filter(user_id = 2)
            self.fields['portfolio2'].queryset = Portfolio.objects.filter(user=user)
            self.fields['portfolio3'].queryset = Portfolio.objects.filter(user=user)
'''

class WorkHistoryForm(forms.ModelForm):
    class Meta:
        model = PartnerWorkHistory
        exclude = ['user']

class EducationForm(forms.ModelForm):
    class Meta:
        model = PartnerEducation
        exclude = ['user']

class LicenseForm(forms.ModelForm):
    class Meta:
        model = PartnerLicense
        exclude = ['user']

class TechniqueForm(forms.ModelForm):
    class Meta:
        model = PartnerTechnic
        exclude = ['user']

