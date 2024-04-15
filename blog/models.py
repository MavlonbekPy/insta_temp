from django.db import models
from django.utils.safestring import mark_safe
from django.core.exceptions import ObjectDoesNotExist
from authentication.models import MyUser


class Post(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/')

    is_published = models.BooleanField(default=True)

    def get_like_count(self):
        return self.likepost_set.count()

    def admin_photo(self):
        return mark_safe('<img src="{}" width="70" />'.format(self.image.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author.user.username} | {self.id} |'

    @classmethod
    def all_(cls):
        query = "SELECT * FROM blog_post"
        return cls.objects.raw(raw_query=query)

    @classmethod
    def get_by_id(cls, id_):
        query = "SELECT * FROM blog_post where id={}".format(id_)
        for i in cls.objects.raw(raw_query=query):
            return i
        raise ObjectDoesNotExist('No such post')


class Comment(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    message = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.user.username


class LikePost(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.user.username


class FollowUser(models.Model):
    follower = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.follower.user.username
