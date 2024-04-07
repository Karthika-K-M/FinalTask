from  django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
             auth.login(request,user)
             return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return redirect('register')
            else:
                 user=User.objects.create_user(username=username,password=password,last_name=last_name,first_name=first_name,email=email)
                 print('resgistration of',username,'is success')
                 user.save();
                 return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def edit_user(request):
    if request.method == 'POST':
        # Process form submission and update user details
        request.user.username = request.POST['username']
        request.user.first_name = request.POST['first_name']
        request.user.last_name = request.POST['last_name']
        request.user.email = request.POST['email']
        password = request.POST['password']
        if password:
            request.user.set_password(password)  # Set new password if provided
        request.user.save()
        messages.success(request, 'Your details have been updated successfully.')
        return redirect('edit_user')  # Redirect to the same page to refresh

    return render(request, 'edit_user.html')
# Create your views here.
