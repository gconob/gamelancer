from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import date

from gamelancer_main.category import *

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    usertype = models.SmallIntegerField(default=0)
    companytype = models.SmallIntegerField(default=0)
    profile_complete = models.SmallIntegerField(default=0)
    cell_phone_number = models.CharField(default='0', max_length=140)
    address1 = models.CharField(default='', max_length=255)
    address2 = models.CharField(default='', max_length=255)
    zipcode = models.CharField(default='', max_length=10)

class Project(models.Model):
    user_id = models.IntegerField(default=0)
    title = models.CharField(max_length=140)
    desc = models.TextField()
    '''
    category1 = models.SmallIntegerField(choices=FUNCTIONAL_CATEGORY, default = 0)
    category2 = models.SmallIntegerField(choices=TECHNICAL_CATEGORY, default = 0)
    category3 = models.SmallIntegerField(choices=PLATFORM_CATEGORY, default = 0)
    categery4 = models.SmallIntegerField(choices=GENRE_CATEGORY, default = 0)
    '''
    category1 = models.CharField(choices=FUNCTIONAL_CATEGORY, max_length="32")
    category2 = models.CharField(choices=TECHNICAL_CATEGORY, max_length="32")
    category3 = models.CharField(choices=PLATFORM_CATEGORY, max_length="32")
    categery4 = models.CharField(choices=GENRE_CATEGORY, max_length="32")
    
    region = models.CharField(null=True, max_length = 140)   
    technical_tag1 = models.CharField(null=True, max_length=32)
    technical_tag2 = models.CharField(null=True, max_length=32)
    technical_tag3 = models.CharField(null=True, max_length=32)
    technical_tag4 = models.CharField(null=True, max_length=32)
    technical_tag5 = models.CharField(null=True, max_length=32)
    duration = models.IntegerField(default=0)
    register_time = models.DateTimeField(default= timezone.now)
    work_start_date = models.DateField(null=True)
    closing_date = models.DateField(null=True)
    budget = models.IntegerField(default=0) 
    display = models.BooleanField(default=False)
    
    @property
    def is_past_due(self):
        return date.today() > self.closing_date
    
    

class ProjectConcern(models.Model):
    project_id = models.IntegerField()
    user_id = models.IntegerField()

class ProjectApply(models.Model):
    project_id = models.IntegerField()
    user_id = models.IntegerField()
    budget = models.IntegerField()
    duration = models.IntegerField()
    comment = models.TextField()
    portfolio = models.CharField(max_length=55)
    portfolio_desc = models.TextField()
    
class Portfolio(models.Model):
    user_id = models.IntegerField()
    project_id = models.IntegerField(default=0)
    category = models.CharField(default='0', max_length=140) 
    desc = models.TextField(default='0')
    start_day = models.DateField()
    end_day = models.DateField()
    participation_ratio = models.IntegerField()
    technical_tag = models.CharField(max_length=255)
    image1 = models.ImageField(upload_to='portfolio')
    image2 = models.ImageField(upload_to='portfolio')
    image3 = models.ImageField(upload_to='portfolio')
    image4 = models.ImageField(upload_to='portfolio')
    image5 = models.ImageField(upload_to='portfolio')
    image1desc = models.CharField(max_length=140)
    image2desc = models.CharField(max_length=140)
    image3desc = models.CharField(max_length=140)
    image4desc = models.CharField(max_length=140)
    image5desc = models.CharField(max_length=140)
    
    

    
      
    
'''
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:      
        UserProfile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
   instance.userprofile.save()
'''
#User.profile = property(lambda u : UserProfile.objects.get_or_create(user=u)[0])
    
    
    
    