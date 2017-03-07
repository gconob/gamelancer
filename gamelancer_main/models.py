from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

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
    user_id = models.IntegerField(default=1)
    title = models.CharField(max_length=140)
    desc = models.TextField()
    rootcategory = models.SmallIntegerField(default=0)
    childcategory = models.SmallIntegerField(default = 1)
    region_code1= models.IntegerField(default=0)
    region_code2=models.IntegerField(default = 0)
    technical_tag = models.CharField(max_length=255)
    
class ProjectCategory_Master(models.Model):
    title = models.CharField(max_length=140)
    parent_id = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    register_time = models.DateTimeField(default=timezone.now())
    work_start_date = models.DateField(null=True)
    closing_date = models.DateField(null=True)
    budget = models.IntegerField(default=0)  
     
class ProjectCategory(models.Model):
    project_id = models.IntegerField()
    category_id = models.IntegerField()

    
    
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
    
    
    
    