from django.contrib.auth.models import User
from .models import PrivateNotice

def alarm_cnt(request):
    count =  PrivateNotice.objects.filter(reader=request.user, readyn=False).count()
    return {'alarm_cnt': str(count)}
