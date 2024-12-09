from django.shortcuts import render, redirect
from home.forms import LessonForm

def create_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('update_profile')
    else:
        form = LessonForm()

    return render(request, 'create_lesson.html', {'form': form})
