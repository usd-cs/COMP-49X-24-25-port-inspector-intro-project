from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.utils import timezone

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=128)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

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