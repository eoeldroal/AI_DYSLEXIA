from django.shortcuts import render
from home.models import UserProfile, UserLanguage, CommunityPost

def dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_languages = UserLanguage.objects.filter(user=request.user)
    community_posts = CommunityPost.objects.all()
    completed_lessons = user_profile.completed_lessons.all()
    favorite_language = user_profile.favorite_language

    context = {
        'user_profile': user_profile,
        'user_languages': user_languages,
        'community_posts': community_posts,
        'completed_lessons': completed_lessons,
        'favorite_language': favorite_language,
    }
    return render(request, 'dashboard.html', context)
