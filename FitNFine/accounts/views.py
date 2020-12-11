from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from . import tokens
from . import authenticate

from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# render syntax:
# return render(request,'page.html',context_var_dictionary)

def logout(request):
    auth.logout(request)
    messages.info(request,"You're Logged Out.")
    return redirect("/")

def login(request):
    username=request.POST['username'];
    password=request.POST['pass'];

    #Validation checks
    if(len(username)>50):
        messages.info(request,"Username can't have more than 50 characters!")
    elif(len(username)==0):
        messages.info(request,"Username can't be empty!")
    elif(len(password)<8):
        messages.info(request,"Password can't have less than 8 characters!")
    elif(len(password)>50):
        messages.info(request,"Password can't have more than 50 characters!")
    else:
        if(authenticate.login(request,username, password)):
            messages.info(request,'Login Successful!')
            return redirect("/#features_section")
        else:
            messages.info(request,"Wrong Username or password!")
    return redirect("/")

def register(request):
    username=request.POST['username']
    name=request.POST['name']
    password=request.POST['pass']
    password2=request.POST['pass2']
    email=request.POST['email']
    phone=request.POST['phone']

    #Validation checks
    if(len(username)>50):
        messages.info(request,"Username can't have more than 50 characters!")
    elif(len(username)==0):
        messages.info(request,"Username can't be empty!")

    elif(len(name)==0):
        messages.info(request,"Name can't be empty!")
    elif(len(name)>50):
        messages.info(request,"Name can't have more than 100 characters!")

    elif(len(email)==0):
        messages.info(request,"Email can't be empty!")
    elif(len(email)>250):
        messages.info(request,"Email can't have more than 250 characters!")

    
    elif(len(phone)==0):
        messages.info(request,"Phone Number can't be empty!")
    elif(len(phone)>10):
        messages.info(request,"Phone Number can't have more than 10 characters!")

    elif(len(password)<8):
        messages.info(request,"Password can't have less than 8 characters!")
    elif(len(password)>50):
        messages.info(request,"Password can't have more than 50 characters!")
    elif(password != password2):
        messages.info(request,"Confirm Password doesn't match!")
    
    else:
        names=name.split()
        lname=""
        fname=""
        if len(names)>1:
            lname=names.pop()
            fname=" ".join(names)
        else:
            fname=names[0]

        if(authenticate.hasRegisteredUsername(username)):
            messages.info(request,'This Username is already registered!')
        elif(authenticate.hasRegisteredEmail(email)):
            messages.info(request,'This Email is already registered!')
        elif(authenticate.hasRegisteredPhone(phone)):
            messages.info(request,'This Phone is already registered!')
        else:
            if(authenticate.register(username, fname, lname, password, email, phone)):
                messages.info(request,'Registeration Successful! You will recieve a verification email shortly.')
                return redirect("/#features_section")
            else:
                messages.info(request,"Registeration Failed!")

    return redirect("/")

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and tokens.account_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.info(request,"Email Confirmed. You can login to your account now.")
        return redirect("/#features_section")
    else:
        messages.info(request,"Invalid Activation link!")
        return redirect("/")
