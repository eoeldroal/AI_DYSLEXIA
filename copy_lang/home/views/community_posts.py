from django.shortcuts import render
from home.models import CommunityPost

def community_posts(request):
    posts = CommunityPost.objects.all()
    return render(request, 'community_posts.html', {'posts': posts})
