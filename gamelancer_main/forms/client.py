from django import forms
from gamelancer_main.models import *
from gamelancer_main.category import *
from .html5 import Html5Date

class ProjectRegisterForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = [ 'client', 'partner', 'display']
        widgets = { 'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'제목'}),
                     'desc' : forms.Textarea(attrs={'class':'form-control'}),
                    'duration' : forms.NumberInput(attrs={'class':'form-control'}),
                    'technical_tag':forms.TextInput(attrs={'class':'form-control'}),
                    'category1' : forms.Select(choices=FUNCTIONAL_CATEGORY, attrs={'class':'form-control'}),
                    'category2' : forms.Select(choices=PLATFORM_CATEGORY, attrs={'class':'form-control'}),
                    'category3' : forms.Select(choices=GENRE_CATEGORY, attrs={'class':'form-control'}),
                    'work_start_date': Html5Date(attrs={'class':'form-control'}),
                    'closing_date': Html5Date(attrs={'class':'form-control'}),
                    'budget': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'만원'}),
                    'region': forms.TextInput(attrs={'class':'form-control'}),
                    'client':forms.TextInput(attrs={'class':'form-control'}),
                    'register_time': Html5Date(attrs={'class':'form-control'})

                  }

        labels = {'title': '제목', 'desc':'상세설명', 'duration':'예상기간', 'technical_tag':'기술 태그',
                  'region':'업무지역', 'budget':'예산',
                  'category1':'업무형태', 'category2':'플랫폼', 'category3':'장르',
                  'work_start_date':'예상 업무 시작일',
                  'closing_date':'모집마감일'}


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

class ClientAccountForm(forms.Form):
    account_owner = forms.CharField(max_length=140)
    account_number = forms.CharField(max_length=140)
    bank_name = forms.CharField(max_length=140)

    def clean_account_owner(self):
        if 'account_owner' in self.cleaned_data:
            account_owner = self.cleaned_data['account_owner']
            return account_owner
        else:
            raise forms.ValidationError('예금주를 정확히 적어 주세요')

    def clean_account_number(self):
        if 'account_number' in self.cleaned_data:
            account_number = self.cleaned_data['account_number']
            return account_number
        else:
            raise forms.ValidationError('계좌번호를 정확히 적어 주세요')

    def clean_bank_name(self):
        if 'bank_name' in self.cleaned_data:
            bank_name = self.cleaned_data['bank_name']
            return bank_name
        else:
            raise forms.ValidationError('은행명을 적어 주세요')

class ClientAuthForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['company_name', 'companytype', 'business_registration_number', 'company_representative', 'business_address', 'tax_email', 'document_image']
        widgets = { 'company_name': forms.TextInput(attrs={'class':'form-control'}),
                    'companytype': forms.Select(choices=TEAM, attrs={'class':'form-control'}),
                    'business_registration_number' : forms.TextInput(attrs={'class':'form-control'}),
                    'company_representative': forms.TextInput(attrs={'class':'form-control'}),
                    'business_address': forms.TextInput(attrs={'class':'form-control'}),
                    'tax_email': forms.EmailInput(attrs={'class':'form-control'}),
                    'document_image' : forms.FileInput(attrs={'class':'form-control'})}
        labels = {'company_name':'회사이름', 'companytype':'회사형태', 'company_representative':'대표자', 'business_address':'회사주소',
                    'business_registration_number':'사업자등록번호', 'tax_email':'세금계산서 발행 이메일', 'document_image':'증빙서류 스캔 파일'}

