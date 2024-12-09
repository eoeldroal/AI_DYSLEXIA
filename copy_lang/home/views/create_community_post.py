from django.shortcuts import render, redirect
from home.models import CommunityPost

def create_community_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        user = request.user
        CommunityPost.objects.create(user=user, title=title, content=content)
        return redirect('community_posts')
    return render(request, 'create_community_post.html')
