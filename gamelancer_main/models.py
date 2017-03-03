from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    usertype = models.SmallIntegerField()
    profile_complete = models.SmallIntegerField()
    cell_phone_number = models.CharField(max_length=140)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)

User.profile = property(lambda u : UserProfile.objects.get_or_create(user=u)[0])
    