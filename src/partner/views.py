from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login as auth_login
from django.shortcuts import render, redirect

def index(request):
    """Define index pages"""

    context= {

    }

    return render(request, "partner/index.html", context)
    
def login(request):
    """Login pages"""

    context= {

    }
    if request.method =="GET":
        pass
    elif request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            
            return redirect("/partner/") 
        else:
            context.update({"error": "사용자가 없습니다."})
    
    return render(request, "partner/login.html", context)

def signup(request):
    """Define signup pages"""
    if request.method =="GET":
        pass
    elif request.method =="POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        # print(username, email, password)

        user = User.objects.create_user(username, email, password)


    context={}
    
    return render(request, "partner/signup.html", context)

def logout_view(request):
    """Define logout"""
    logout(request)

    return redirect("/partner/")