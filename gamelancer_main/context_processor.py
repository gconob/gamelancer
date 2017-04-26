from django.contrib.auth.models import User
from .models import PrivateNotice

def alarm_cnt(request):
    count =  PrivateNotice.objects.filter(reader=request.user.id, readyn=False).count()
    #여기서 request.user를 쓰면 에러난다
    return {'alarm_cnt': str(count)}
