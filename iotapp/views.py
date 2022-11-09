from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request,'home.html')

def configure(request):
    return render(request,'configure.html')

