from django.shortcuts import render, redirect
from home.forms import LessonTagForm

def create_lesson_tag(request):
    if request.method == 'POST':
        form = LessonTagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_lesson')
    else:
        form = LessonTagForm()

    return render(request, 'create_lesson_tag.html', {'form': form})
