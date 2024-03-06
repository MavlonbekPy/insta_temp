from django.shortcuts import render, redirect
from .models import Post, FollowUser
from django.contrib.auth.decorators import login_required
from authentication.models import MyUser


@login_required(login_url='auth/login')
def home_view(request):
    posts = Post.objects.filter(is_published=True)
    users = MyUser.objects.all()[:4]
    profile = MyUser.objects.filter(user=request.user).first()
    return render(request, 'index.html', context={'posts': posts, 'users': users, 'profile': profile})


@login_required(login_url='auth/login')
def follow(request):
    follower = MyUser.objects.filter(user=request.user).first()
    following = MyUser.objects.filter(id=request.GET.get('following_id')).first()
    obj = FollowUser.objects.create(follower=follower, following=following)
    obj.save()
    return redirect('/')
