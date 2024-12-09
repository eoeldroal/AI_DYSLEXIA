from django.shortcuts import render, redirect
from home.forms import LanguageForm

def language(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = LanguageForm()

    return render(request, 'language.html', {'form': form})
