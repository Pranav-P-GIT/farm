from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import FarmProduct

# Create your views here.


def index(request):
    
 
        data=FarmProduct.objects.all()

  


        return render(request,"index.html",{"pro":data})

def login(request):
    if request.method=="POST":
        username=request.POST["uname"]
        password=request.POST["pass"]
        check=auth.authenticate(username=username,password=password)
        if check is not None:
            auth.login(request,check)
            return redirect("/")
        else:
            msg="Invalid Username Or Password"
            return render(request,"login.html",{"msg":msg})
    else:
        return render(request,"login.html")
    
    
def register(request):
    if request.method=="POST":
        username=request.POST["uname"]
        firstname=request.POST["fname"]
        secondname=request.POST["sname"]
        email=request.POST["email"]
        password=request.POST["pass"]
        repassword=request.POST["repass"]
        ucheck=User.objects.filter(username=username)
        echeck=User.objects.filter(email=email)
        if ucheck:
            msg="Username Exits"
            return render(request,"register.html",{"msg":msg})
        elif echeck:
            msg="Email Exits"
            return render(request,"register.html",{"msg":msg})
        elif password=="" or password!=repassword:
            msg="Invalid Password"
            return render(request,"register.html",{"msg":msg})
        else:
            user=User.objects.create_user(username=username,first_name=firstname,last_name=secondname,email=email,password=password)
            user.save();
            return redirect("/")
    else:
        return render(request,"register.html")
    
def logout(request):
    auth.logout(request)
    return redirect("/")
    
def test(request):
    if request.method=="POST":
        search=request.POST["msg"]
        data=FarmProduct.objects.filter(name__istartswith=search)
        return render(request,"results.html",{"pro":data})
   


