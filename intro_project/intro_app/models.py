from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    contents = models.TextField()
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    contents = models.TextField()
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(default=timezone.now)


class User(models.Model):
	user_id = models.IntegerField(primary_key=True)
	email = models.EmailField(unique=True, max_length=255, null=True, blank=True)
	name = models.CharField(max_length=255, null=True, blank=True)
	admin = models.BooleanField(default=False)