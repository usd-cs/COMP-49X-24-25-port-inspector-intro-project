from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from intro_app.models import User 

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Find all users with admin=True
        admin_users = User.objects.filter(admin=True)
        
        for user in admin_users:
            django_user, created = User.objects.get_or_create(email=user.email)
            django_user.is_superuser = True
            django_user.is_staff = True
            django_user.save()

            self.stdout.write(self.style.SUCCESS(f'User {user.email} is now a superuser.'))
