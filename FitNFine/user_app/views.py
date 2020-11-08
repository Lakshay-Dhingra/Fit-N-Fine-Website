from django.shortcuts import render

# Create your views here.
def profile(request,username):
    return render(request,'user_app/profile.html')

def calorieTracker(request):
    return render(request,'user_app/calorie-tracker.html')