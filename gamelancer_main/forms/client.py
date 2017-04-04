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

