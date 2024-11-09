from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    admin = models.BooleanField(default=False)
    password = models.CharField(max_length=128)
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    contents = models.TextField()
    user = models.ForeignKey('intro_app.User', on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    contents = models.TextField()
    user = models.ForeignKey('intro_app.User', on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey('intro_app.Post', on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(default=timezone.now)