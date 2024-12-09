from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) #User와 onetoone
    fullName = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=100,default="")
    Email=models.EmailField(max_length=100)
    language_level_choices = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    language_level = models.CharField(max_length=20, choices=language_level_choices)
    
    # New fields for progress tracking and personalization
    completed_lessons = models.ManyToManyField('Lesson', blank=True, related_name='completed_by_users')
    favorite_language = models.ForeignKey('Language', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username
 