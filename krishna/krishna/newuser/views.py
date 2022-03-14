from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method=='POST':
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        un=request.POST['username']
        em=request.POST['email']
        pw=request.POST['password']
        pw1=request.POST['password1']
        if pw == pw1:
            if User.objects.filter(username=un).exists():
                messages.info(request, 'Username available')
                return redirect('register')
            elif User.objects.filter(email=em).exists():
                messages.info(request, 'Email available')
                return redirect('register')
            else:
                user = User.objects.create_user(username=un,password=pw,first_name=fn,last_name=ln,email=em)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not match')
            return redirect('register')

    return render(request, 'register.html')
def login(request):
    if request.method=='POST':
        un=request.POST['username']
        pw=request.POST['password']
        user=auth.authenticate(username=un, password=pw)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Incorrect value')
            return redirect('login')
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')