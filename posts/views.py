from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Post

def view_post(request, id):
    post = Post.objects.get(id=id)
    
    context = {'post':post}
    return render(request, 'posts/post_detail.html', context)


def like_post(request, id):
    if request.method == "POST":
        instance = Post.objects.get(id=id)
        if not instance.likes.filter(id=request.user.id).exists():
            instance.likes.add(request.user)
            instance.save() 
            return render( request, 'posts/partials/icons_area.html', context={'post':instance})
        else:
            instance.likes.remove(request.user)
            instance.save() 
            return render( request, 'posts/partials/icons_area.html', context={'post':instance})