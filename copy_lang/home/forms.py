from .models import LessonTag
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db.models import fields
from .models import UserProfile, Lesson, Language, LessonTag, UserLanguage

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

# language_app/forms.py
class LoginForm(AuthenticationForm):
    # You can customize the form if needed (e.g., add extra fields, widgets, etc.)
    class Meta:
        model = User  # Assuming User model is imported
        fields = ['username', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['fullName', 'language_level',
                  'completed_lessons', 'favorite_language']

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'content', 'difficulty', 'tags']

    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter the lesson title'}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Enter the lesson content'}))

    difficulty = forms.ChoiceField(choices=Lesson.difficulty_choices)
    tags = forms.ModelMultipleChoiceField(
        queryset=LessonTag.objects.all(), widget=forms.CheckboxSelectMultiple)

class LanguageForm(forms.ModelForm):
    class Meta:
        model = UserLanguage
        fields = ['language', 'user']

class FavoriteLanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name']

class LessonTagForm(forms.ModelForm):
    class Meta:
        model = LessonTag
        fields = ['name']

    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter tag name'}))