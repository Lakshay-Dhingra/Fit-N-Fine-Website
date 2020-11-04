from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Username and password will be in default User Model Provided by django
# Create your models here.
class UserDetails(models.Model):
    username=models.CharField(primary_key=True, max_length=50)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField(max_length=254, unique=True)
    
    phone=models.PositiveBigIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)], unique=True)
    about_me=models.TextField(max_length=500, null=True, blank=False)

    country=models.CharField(max_length=100, null=True, blank=False)
    city=models.CharField(max_length=100, null=True, blank=False)

    FITNESS_GOAL_DEFAULT='Improve My Overall Health'
    FITNESS_GOAL_CHOICES = [
        (FITNESS_GOAL_DEFAULT, 'Improve My Overall Health'),
        ('Improve My Mental Health', 'Improve My Mental Health'),
        ('Spread Awareness About Health and Fitness', 'Spread Awareness About Health and Fitness'),
        ('Track My Calorie Intake and Burn', 'Track My Calorie Intake and Burn'),
        ('Give Health Consultancy', 'Give Health Consultancy'),
        ('Body Building', 'Body Building'),
        ('Other', 'Other'),
    ]
    fitness_goal=models.CharField(max_length=50, choices=FITNESS_GOAL_CHOICES, default=FITNESS_GOAL_DEFAULT)

    USER_TYPE_DEFAULT='Fitness Enthusiast'
    USER_TYPE_CHOICES = [
        (USER_TYPE_DEFAULT, 'Fitness Enthusiast'),
        ('Fitness Intstructor', 'Fitness Intstructor'),
        ('Fitness Blogger', 'Fitness Blogger'),
        ('Yoga Intstructor', 'Yoga Intstructor'),
        ('Nutritionist', 'Nutritionist'),
        ('Physiotherapist', 'Physiotherapist'),
        ('Psychologist', 'Psychologist'),
        ('Ayurvedic Doctor', 'Ayurvedic Doctor'),
        ('Other Specialized Doctor', 'Other Specialized Doctor'),
    ]
    user_type=models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default=USER_TYPE_DEFAULT)
    
    DEFAULT_GENDER='U'
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        (DEFAULT_GENDER, 'Unknown'),
    ]
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES, default=DEFAULT_GENDER)

    age=models.PositiveSmallIntegerField(validators=[MaxValueValidator(150),MinValueValidator(5)], null=True)
    height=models.FloatField(validators=[MaxValueValidator(120),MinValueValidator(20)], null=True)
    weight=models.FloatField(validators=[MaxValueValidator(250),MinValueValidator(5)], null=True)

    profile_pic=models.ImageField(upload_to="profile_pics/", null=True)

    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural='User Details'