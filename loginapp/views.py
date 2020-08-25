from django.contrib.auth.models import User,auth

from.models import signup

from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index (request):
    return render(request,"index.html")

def signup(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        address=request.POST['address']
        address2=request.POST['address2']
        mobile=request.POST['mobile']
        city=request.POST['city']
        state=request.POST['state']
        zip=request.POST['zip']
        user = User.objects.create_user(username=email, password=password, email=email)
        user.save()
        return render(request, "aftersignup.html")
    else:
        return render(request, "index.html")


def afterSignup(request):
    return render(request, "aftersignup.html")


def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request, "login.html", {"login": "successfully login","user":user})


        else:
            return render(request,"login.html", {"error":"invalid credentials"})


    else:
        return render(request,"login.html")


