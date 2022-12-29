from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password= request.POST['password']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("user authenticate")
            return redirect("show")

        else:
            messages.info(request,"invalid credentials",'login.html')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        if password==confirm_password:
            if len(password)<8:
                messages.info(request,"Password must be 8 or more character long",'register.html')
                return redirect('register')
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is taken",'register.html')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken",'register.html')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,"password not matching",'register.html')
        return redirect('show') #once registration done go home page
    else:
        return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect("index")