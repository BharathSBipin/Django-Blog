from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Blog,Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib import messages
# Create your views here.

def home(request):
    blog = Blog.objects.all()
    context={
        "blog":blog

    }

    return render(request,"home.html",context)

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def content(request,id):
    blog=Blog.objects.get(id=id)
    comment=Comment.objects.all().order_by("-id")
    context={
        "blog":blog,
        "comment":comment,
    }
    return render(request,"blogcontent.html",context)

def signup(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        email=request.POST.get("email")
        password=request.POST.get("password")

        user=User.objects.create_user(first_name=fname,username=email,password=password)

        user.save()
        messages.add_message(request, messages.INFO, "Sucessfully Created User")
        return redirect("home")
    
    return render(request,"signup.html")

def login(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            messages.add_message(request, messages.INFO, "Login Sucessfull")
            auth_login(request, user)
        else:
            messages.error(request,"ERROR INVALID LOGIN")
        return redirect("home")

    return render(request,"login.html")

def Logout(request):
    logout(request)
    messages.add_message(request, messages.INFO, "Logout Sucessfull")
    return redirect("home")


def comment(request):
    if request.method=="POST":
        name = request.user
        blogid = request.POST.get("blogid")
        comment = request.POST.get("comment")
        blog=Blog.objects.get(id=blogid)
        comment=Comment(name=name,blogparent=blog,comment=comment)
        comment.save()
        messages.success(request,"Commented Sucessfully")

    return  redirect(f"content/{blogid}")