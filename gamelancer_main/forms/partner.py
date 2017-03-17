from django import forms
from django.forms import  ModelForm, Textarea
from gamelancer_main.models import Portfolio
from .html5 import Html5Date

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        exclude = ['user']
        widgets = {'desc': Textarea(attrs={'cols':80, 'rows':20}), 'start_day' : Html5Date, 'end_day':Html5Date }

    def clean_technical_tag(self):
        if 'technical_tag' in self.cleaned_data:
            technical_tag = self.cleaned_data['technical_tag']
            tags = technical_tag.split()
            if len(tags) > 5 :
                raise forms.ValidationError("기술 태그는 최대 5개까지 적을 수 있습니다")
