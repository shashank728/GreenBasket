from django.shortcuts import render, redirect
from django.contrib import auth

def login(request):
    return render(request,"accounts/login.html")

def register(request):
    return render(request,"accounts/signup.html")

def profile(request):
    return render(request, "accounts/profile.html")

def logout(request):
    auth.logout
    return redirect("home")
