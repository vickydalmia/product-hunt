from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def accounts(request):
    return render(request, 'home.html')



def signup(request):
    if request.method == 'POST':
        #do something
        if request.POST['userpassword'] == request.POST['confirmuserpassword']:
            try:
                u = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username already has been taken'})
            except User.DoesNotExist:
                u = User.objects.create_user(request.POST['username'], password=request.POST['userpassword'])
                auth.login(request, u)
                return redirect('createproduct')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Password Validaton Failed'})
    else:
        return render(request, 'accounts/signup.html')



def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['userpassword'])
        if user is not None:
            auth.login(request, user)
            return redirect('createproduct')
        else:
            return render(request, 'accounts/login.html', {'error':'Username or password is incorrect or doesn\'t exist'})
    else:
        return render(request, 'accounts/login.html')



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
