from django.shortcuts import render, redirect
from . import userdata
# render syntax:
# return render(request,'page.html',context_var_dictionary)

def profile(request,un):
    public_user_details=userdata.getUserPublicDataDict(un)
    return render(request,'user_app/profile_page.html',public_user_details)

def calorieTracker(request):
    return render(request,'user_app/calorie-tracker.html',{"List":[1,2,3,4]})