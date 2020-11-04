from django.contrib import admin
from .models import UserDetails

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('username','user_type','gender','fitness_goal','country','created_at')
    list_filter=['user_type','gender','fitness_goal','age','country','city','height','weight','created_at']

admin.site.register(UserDetails,UserDetailsAdmin)