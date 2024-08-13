# user_messages/forms.py

from django import forms
from .models import UserMessage

class MessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ['receiver', 'content']
