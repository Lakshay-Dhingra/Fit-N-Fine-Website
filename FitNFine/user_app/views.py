from django.shortcuts import render, redirect

# render syntax:
# return render(request,'page.html',context_var_dictionary)

def profile(request,un):
    return render(request,'user_app/profile_page.html',{"username":un})

def calorieTracker(request):
    return render(request,'user_app/calorie-tracker.html')