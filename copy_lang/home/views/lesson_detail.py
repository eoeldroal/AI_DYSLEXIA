from django.shortcuts import render, get_object_or_404
from home.models import Lesson, UserProfile

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.completed_lessons.add(lesson)
    return render(request, 'lesson_detail.html', {'lesson': lesson})
