from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from authentication.models import MyUser


@login_required(login_url='auth/login')
def home_view(request):
    posts = Post.objects.filter(is_published=True)
    users = MyUser.objects.all()[:4]
    profile = MyUser.objects.filter(user=request.user).first()
    return render(request, 'index.html', context={'posts': posts, 'users': users, 'profile': profile})
