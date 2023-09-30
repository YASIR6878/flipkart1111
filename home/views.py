from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout as django_logout

def index(request):
    if request.user.is_anonymous:
        return redirect('loginuser')
    return render(request, 'index.html')

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('loginuser')
    return render(request, 'login.html')

def signup(request):
  if request.method=="POST":
        username = request.POST.get('name')
        password = request.POST.get('pass')
        email=request.POST.get('email')
        if User.objects.filter(email=email).exists():
            messages.info(request,'Account Already Exists!')
            return redirect('signup')
        elif User.objects.filter(username=username).exists():
            messages.info(request,'Username Already Exists!')
            return render('signup')
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            messages.success(request,'Congratulations')
            return redirect('loginuser')
  else:
      return render(request,'signup.html')

def logout(request):
    django_logout(request)
    return redirect('loginuser')
