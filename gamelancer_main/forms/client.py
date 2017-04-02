from django import forms
from gamelancer_main.models import *
from gamelancer_main.category import *
from .html5 import Html5Date

class ProjectRegisterForm(forms.Form):
    title = forms.CharField(label='제목 ', max_length=140)
    desc = forms.CharField(label='상세설명 ', widget=forms.Textarea)
    duration = forms.IntegerField(label="예상기간 ")
    technical_tag = forms.CharField(label="기술태그", max_length=128)
    closing_date = forms.DateField(label="마감일", widget=Html5Date)
    work_start_date = forms.DateField(label="예상업무시작일 ", widget=Html5Date)
    budget = forms.IntegerField(label="예산")
    category1 = forms.ChoiceField(choices=FUNCTIONAL_CATEGORY, label="기능별 ", initial='', widget=forms.Select())
    category2 = forms.ChoiceField(choices=PLATFORM_CATEGORY, label="플랫폼별 ", initial='', widget=forms.Select())
    category3 = forms.ChoiceField(choices=GENRE_CATEGORY, label="장르별 ", initial='', widget=forms.Select())

    def clean_closing_date(self):
        if 'closing_date' in self.cleaned_data:
            closing_date = self.cleaned_data['closing_date']
            if date.today() >= closing_date:
                raise forms.ValidationError("마감일은 오늘보다 나중이어야 합니다")
            return closing_date
        raise forms.ValidationError("마감일을 지정해야 합니다")

    def clean_work_start_date(self):
        if 'work_start_date' in self.cleaned_data:
            work_start_date = self.cleaned_data['work_start_date']
            if 'closing_date' in self.cleaned_data:
                closing_date = self.cleaned_data['closing_date']
                if work_start_date <= closing_date:
                    raise forms.ValidationError("업무시작일은 마감일보다 나중이어야 합니다")
                return work_start_date
        raise forms.ValidationError("업무시작일을 지정해야 합니다")

class ClientIntroForm(forms.Form):
    desc = forms.Textarea()
    address1 = forms.CharField(max_length=140)
    address2 = forms.CharField(max_length=140)
