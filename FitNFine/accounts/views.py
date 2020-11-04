from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

from . import authenticate
# render syntax:
# return render(request,'page.html',context_var_dictionary)

def logout(request):
    auth.logout(request)
    return redirect("/")

def login(request):
    username=request.POST['username'];
    password=request.POST['pass'];

    #Validation checks
    if(len(username)>50):
        messages.info(request,"Invalid Username! Username can't have more than 50 characters.")
    elif(len(username)==0):
        messages.info(request,"Invalid Username! Username can't be empty.")
    elif(len(password)<8):
        messages.info(request,"Invalid Password! Password can't have less than 8 characters.")
    elif(len(password)>50):
        messages.info(request,"Invalid Password! Password can't have more than 50 characters.")
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
        messages.info(request,"Invalid Username! Username can't have more than 50 characters.")
    elif(len(username)==0):
        messages.info(request,"Invalid Username! Username can't be empty.")

    elif(len(name)==0):
        messages.info(request,"Invalid Name! Name can't be empty.")
    elif(len(name)>50):
        messages.info(request,"Invalid Name! Name can't have more than 100 characters.")

    elif(len(email)==0):
        messages.info(request,"Invalid Email! Email can't be empty.")
    elif(len(email)>250):
        messages.info(request,"Invalid Email! Email can't have more than 250 characters.")

    
    elif(len(phone)==0):
        messages.info(request,"Invalid Phone Number! Phone Number can't be empty.")
    elif(len(phone)>10):
        messages.info(request,"Invalid Phone Number! Phone Number can't have more than 10 characters.")

    elif(len(password)<8):
        messages.info(request,"Invalid Password! Password can't have less than 8 characters.")
    elif(len(password)>50):
        messages.info(request,"Invalid Password! Password can't have more than 50 characters.")
    elif(password != password2):
        messages.info(request,"Invalid Password! Confirm Password doesn't match.")
    
    else:
        names=name.split()
        lname=""
        fname=""
        if len(names)>1:
            lname=names.pop()
            fname=names.join(" ")
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
                messages.info(request,'User Registeration Successful!')
                return redirect("/#features_section")
            else:
                messages.info(request,"User Registeration Failed!")

    return redirect("/")

