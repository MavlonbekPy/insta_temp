from django.shortcuts import render, redirect, HttpResponse
from .models import Post, FollowUser, LikePost, Comment
from django.contrib.auth.decorators import login_required
from authentication.models import MyUser
from django.contrib.postgres.search import SearchVector


@login_required(login_url='auth/login')
def home_view(request):
    profile = MyUser.objects.filter(user=request.user).first()
    following_users = FollowUser.objects.filter(follower=profile).values_list('following', flat=True)
    suggested_users = MyUser.objects.exclude(id__in=following_users).exclude(id=profile.id)[:5]
    posts = Post.objects.filter(is_published=True, author__in=following_users)
    comments = Comment.objects.all()

    for post in posts:
        post.comments = Comment.objects.filter(post_id=post.id)

    context = {'posts': posts, 'profile': profile, 'suggested_users': suggested_users}

    if request.method == 'POST':
        data = request.POST
        obj = Comment.objects.create(author=profile, message=data['message'], post_id=data['post_id'])
        obj.save()
        return redirect(f'/#{data["post_id"]}')

    return render(request, 'index.html', context=context)


@login_required(login_url='auth/login')
def follow_unfollow(request):
    follower = MyUser.objects.filter(user=request.user).first()
    following = MyUser.objects.filter(id=request.GET.get('following_id')).first()

    try:
        follow_obj = FollowUser.objects.get(follower=follower, following=following)
        follow_obj.delete()
        is_following = False
    except FollowUser.DoesNotExist:
        follow_obj = FollowUser.objects.create(follower=follower, following=following)
        follow_obj.save()
        is_following = True

    context = {'is_following': is_following}
    return redirect('/')


@login_required(login_url='auth/login')
def blog_search_view(request):
    query = request.GET.get('text')
    users = MyUser.objects.all()

    if query:
        query = query.replace('+', ' ')
        users = users.annotate(search=SearchVector('user__username')).filter(search__icontains=query)
    return render(request, 'index.html', {'users': users})


@login_required(login_url='auth/login')
def like(request):
    author = MyUser.objects.filter(user=request.user).first()
    post_id = request.GET.get('post_id')
    post = Post.objects.filter(id=post_id).first()

    if not post:
        return redirect('/')

    like_obj, created = LikePost.objects.get_or_create(author=author, post=post)

    if not created:
        like_obj.delete()
    else:
        like_obj.save()

    return redirect(f'/#{post_id}')


def settings_view(request):
    return render(request, 'setting.html')

# def test_sql(r):
#     post = Post.get_by_id(1)
#     print(post.image, post.created_at)
#     # for post in posts:
#     #     print(post.id, post.image, post.created_at)
#     return HttpResponse('Ok')
