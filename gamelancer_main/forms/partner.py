from django import forms
from django.forms import  ModelForm, Textarea
from gamelancer_main.models import Portfolio
from .html5 import Html5Date

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        exclude = ['user']
        widgets = {'desc': Textarea(attrs={'cols':80, 'rows':20}), 'start_day' : Html5Date, 'end_day':Html5Date }

