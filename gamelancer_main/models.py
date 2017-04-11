from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import date
from django.conf import settings
from gamelancer_main.category import *

class Profile(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usertype = models.SmallIntegerField(default=0)    
    desc = models.TextField(null=True)
    companytype = models.CharField(max_length=64, null=True)
    establish_date = models.DateField(null=True)
    email = models.EmailField(null=True)
    identity_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    contact_verified = models.BooleanField(default=False)
    profile_complete = models.BooleanField(default=False)
    cell_phone_number = models.CharField(max_length=140, null=True)
    phone_number = models.CharField(max_length=140,null=True)
    fax_number = models.CharField(max_length=140, null=True)
    address1 = models.CharField(max_length=255, null=True)
    address2 = models.CharField(max_length=255, null=True)
    zipcode = models.CharField(max_length=10, null=True)
    image = models.ImageField(upload_to='user', null=True)
    account_bank = models.CharField(max_length=64, null=True)
    account_owner_name = models.CharField(max_length=64, null=True)
    account_number = models.CharField(max_length=64, null=True)
    company_name = models.CharField(max_length=64, null=True)
    business_registration_number = models.CharField(max_length=64, null=True)
    company_representative = models.CharField(max_length=64,null=True)
    business_address = models.CharField(max_length=128, null=True)
    tax_email=models.EmailField(null=True)
    document_image = models.ImageField(upload_to='document', null=True)

        
    def __str__(self):
        return self.user.username

class Project(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="client")
    partner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='partner', null=True)  # 계약이 되었으면 파트너가 된다. 계약이 안되면 apply 테이블에 있다
    title = models.CharField(max_length=140)
    desc = models.TextField()
    
    category1 = models.CharField(choices=FUNCTIONAL_CATEGORY, max_length="32", default="무관")    
    category2 = models.CharField(choices=PLATFORM_CATEGORY, max_length="32", default="무관" )
    category3 = models.CharField(choices=GENRE_CATEGORY, max_length="32", default="무관")
    
    region = models.CharField(null=True, max_length = 140)   
    technical_tag  = models.CharField(null=True, max_length=128)    
    duration = models.IntegerField(default=0)
    register_time = models.DateTimeField(default= timezone.now)
    work_start_date = models.DateField(null=True)
    closing_date = models.DateField(null=True)
    budget = models.IntegerField(default=0) 
    display = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    @property
    def is_past_due(self):
        return date.today() > self.closing_date
    
    @property
    def get_tag_list(self):
        return self.technical_tag.split(",")

class ProjectComment(models.Model): #프로젝트 댓글
    project = models.ForeignKey(Project)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    parent_id = models.IntegerField(default=0, null=False) #댓글의 댓글일 경우. 0이면 최초댓글
    secret = models.BooleanField(default=False) #비밀댓글
    desc = models.TextField()
    
    def __str__(self):
        return self.project.title + "-" + self.user.username + "-" + self.desc
  
    
class ProjectConcern(models.Model):  # 관심 프로젝트 등록
    project  = models.ForeignKey(Project)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

class Portfolio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)    
    title = models.CharField(max_length=32)
    category1 = models.CharField(choices=FUNCTIONAL_CATEGORY, max_length="32", default="무관")    
    category2 = models.CharField(choices=PLATFORM_CATEGORY, max_length="32", default="무관")
    category3 = models.CharField(choices=GENRE_CATEGORY, max_length="32", default="무관")
    desc = models.TextField(null=True)
    start_day = models.DateField(null=True)
    end_day = models.DateField(null=True)
    participation_ratio = models.IntegerField()
    technical_tag = models.CharField(null=True, max_length=128)    
    image1 = models.ImageField(upload_to='portfolio', null=True)
    image2 = models.ImageField(upload_to='portfolio', null=True)
    image3 = models.ImageField(upload_to='portfolio', null=True)
    image4 = models.ImageField(upload_to='portfolio', null=True)
    image5 = models.ImageField(upload_to='portfolio', null=True)
    image1desc = models.CharField(max_length=140, null=True)
    image2desc = models.CharField(max_length=140, null=True)
    image3desc = models.CharField(max_length=140, null=True)
    image4desc = models.CharField(max_length=140, null=True)
    image5desc = models.CharField(max_length=140, null=True)
    
    def __str__(self):
        return self.user.username + '-' +  self.title
    
class ProjectApply(models.Model):
    project = models.ForeignKey(Project)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    budget = models.IntegerField()
    duration = models.IntegerField()
    comment = models.TextField()
    portfolio1 = models.ForeignKey(Portfolio, related_name='portfolio1', null=True)
    portfolio2 = models.ForeignKey(Portfolio, related_name='portfolio2', null=True)
    portfolio3 = models.ForeignKey(Portfolio, related_name='portfolio3', null=True)
    portfolio_desc = models.TextField()
    
    def __str__(self):
        return self.project.title + '-' + self.user.username + self.comment 
    
class PartnerTechnic(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    type = models.CharField(max_length=140)
    level = models.CharField(choices=TECH_LEVEL, max_length=32)
    time = models.CharField(choices=TIME, max_length=64)
    main = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + '-' + self.type + '(main:' + self.main + ')'

#경력
class PartnerWorkHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    company = models.CharField(max_length=140)
    department = models.CharField(max_length=140)
    title = models.CharField(max_length=140)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.user.username + '-' + self.company
    
class PartnerEducation(models.Model): #파트너 학력
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    school = models.CharField(max_length=140)
    major = models.CharField(max_length=64)
    degree = models.CharField(choices=DEGREE, max_length=32)    
    type = models.CharField(choices=SCHOOL, max_length=140)
    status = models.CharField(choices=SCHOOL_STATUS, max_length=140)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.user.username + '-' + self.school
    
class PartnerLicense(models.Model): #파트너 자젹증
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=64) #자젹증이름
    level = models.CharField(max_length=64, null=True) #자젹증 레벨
    institution = models.CharField(max_length=64, null=True) #발급기관

    def __str__(self):
        return self.user.username + '-' + self.title
    
class Evaluation(models.Model): #평가사항
    evaluator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="evaluator")
    evaluated = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="evaluated")
    score = models.FloatField() #점수 0 ~ 5 (5점만점)
    desc = models.TextField() #평가 설명

class PublicNotice(models.Model): #공지사항
    title = models.CharField(max_length=64)
    desc = models.TextField()
    notice_date = models.DateField()
    display = models.BooleanField()

class PrivateNotice(models.Model): #개인에게 각각 보내주는 공지 (프로젝트 등록 등)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=64)
    desc = models.TextField()
    notice_time = models.DateTimeField()

