from django.contrib import admin
from .models import Post, Comment, FollowUser, LikePost


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'admin_photo', 'created_at')


class FollowUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'follower_username', 'created_at')

    def follower_username(self, obj):
        return obj.follower.user.username


admin.site.register(Post, PostAdmin)
admin.site.register(FollowUser, FollowUserAdmin)
admin.site.register(LikePost)
