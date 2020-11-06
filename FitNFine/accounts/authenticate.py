from django.contrib.auth.models import User,auth
from main_app.models import UserDetails
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from . import tokens

def sendConfirmEmail(user,name,userEmail):
    template=render_to_string('accounts/email_template.html',
        {
            'name':name,
            'user':user,
            'token':tokens.account_token.make_token(user),
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'domain': '127.0.0.1:8000',
        })
    email = EmailMessage(
        "Verify Your Fit N' Fine account",
        template,
        settings.EMAIL_HOST_USER,
        [userEmail],
    )
    email.fail_silently=False
    email.send()

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
        user.is_active=False
        user.save()
        userdetails.save()
        sendConfirmEmail(user,fname,email)
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