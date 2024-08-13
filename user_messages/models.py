# user_messages/models.py

from django.conf import settings
from django.db import models

class UserMessage(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)  # Usa AUTH_USER_MODEL
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)  # Usa AUTH_USER_MODEL
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)  

    def __str__(self):
        return f'Message from {self.sender} to {self.receiver}'
