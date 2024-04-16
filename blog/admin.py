from django.contrib import admin
from .models import Post, Comment, FollowUser, LikePost


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'admin_photo', 'created_at')


class FollowUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'follower_username', 'following', 'created_at')

    def follower_username(self, obj):
        return obj.follower.user.username


class LikePostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'created_at')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'created_at')


admin.site.register(Post, PostAdmin)
admin.site.register(FollowUser, FollowUserAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(LikePost, LikePostAdmin)
