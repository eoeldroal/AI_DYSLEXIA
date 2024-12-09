from django.shortcuts import render, redirect
from home.forms import FavoriteLanguageForm

def select_favorite_language(request):
    if request.method == 'POST':
        form = FavoriteLanguageForm(request.POST)
        if form.is_valid():
            user_language = form.save(commit=False)
            user_language.user = request.user
            user_language.save()
            return redirect('index')
    else:
        form = FavoriteLanguageForm()

    return render(request, 'select_favorite_language.html', {'form': form})
