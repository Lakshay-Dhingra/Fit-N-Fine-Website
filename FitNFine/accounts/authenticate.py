from django.contrib.auth.models import User,auth
from main_app.models import UserDetails

def login(request,username, password):
    user=auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request,user)
        return True
    else:
        return False

def register(username,fname,lname,password,email,phone):
    try:
        user=User.objects.create_user(username=username,password=password,email=email)
        userdetails=UserDetails(username=username,firstname=fname,lastname=lname,email=email,phone=phone)
        user.save()
        userdetails.save()
        return True
    except:
        return False

def hasRegisteredUsername(username):
    try:
        UserDetails.objects.get(username=username)
        return True
    except:
        return False

def hasRegisteredEmail(email):
    try:
        UserDetails.objects.get(email=email)
        return True
    except:
        return False

def hasRegisteredPhone(phone):
    try:
        UserDetails.objects.get(phone=phone)
        return True
    except:
        return False