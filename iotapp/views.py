from django.shortcuts import render,redirect
# Create your views here.
from django.contrib.auth.models import User
from iotapp.models import Token
def index(request):
    user_id = request.user.id
    token = Token.objects.filter(user_id=user_id).values()
    print(token[0]['token'])
    return render(request,'home.html', {"token": token[0]['token'],})

def setting(request):
    return render(request,'setting.html')

def configure(request):
    User_id= request.user.id
    if request.method=='POST':
        token=request.POST.get('token')
        en=Token.objects.create(token=token,user_id=User_id)
        en.save()
    return render(request,'configure.html')
