from django.contrib import admin
from .models import Post, Comment, FollowUser, LikePost

admin.site.register(Post)
admin.site.register(FollowUser)
