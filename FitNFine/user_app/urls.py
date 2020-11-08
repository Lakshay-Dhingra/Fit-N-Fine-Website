from django.urls import path
from . import views
urlpatterns = [
    path('profile/<username>/', views.profile, name='profile'),
    path('calorie-tracker/', views.calorieTracker, name='calorie-tracker'),
]