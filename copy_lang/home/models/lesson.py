from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    difficulty_choices = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    difficulty = models.CharField(max_length=20, choices=difficulty_choices)
    created_at = models.DateTimeField(auto_now_add=True)
  
    # New field for tags or categories
    tags = models.ManyToManyField('LessonTag', blank=True)

    def __str__(self):
        return self.title
