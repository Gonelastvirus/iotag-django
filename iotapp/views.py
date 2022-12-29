from django.shortcuts import render,redirect
# Create your views here.
from django.contrib.auth.models import User
#from iotapp.models import Token
def index(request):
    return render(request,'index.html')

def show(request):
    user_id = request.user.id
    username = User.objects.get(id=user_id)
    print(username)
    #if len(token)!=0:
        #return render(request,'home.html', {"token": token[0]['token'],})
    #else:
    return render(request,'show.html',{'username':username})#, {"token": token[0]['token'],})

def setting(request):
    return render(request,'setting.html')

def configure(request):
    User_id= request.user.id
    if request.method=='POST':
        token=request.POST.get('token')
        en=Token.objects.create(token=token,user_id=User_id)
        en.save()
    return render(request,'configure.html')
