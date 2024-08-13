# accounts/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Cambia 'user_set' a 'customuser_set'
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',  # Cambia 'user_set' a 'customuser_permissions_set'
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )
