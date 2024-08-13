# user_messages/views.py

from django.shortcuts import render, redirect
from .models import UserMessage
from .forms import MessageForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def message_list(request):
    # Obtener mensajes donde el usuario es el receptor
    messages = UserMessage.objects.filter(receiver=request.user)
    unread_count = messages.filter(read=False).count()

    # Marcar los mensajes no leídos como leídos
    unread_messages = messages.filter(read=False)
    unread_messages.update(read=True)

    return render(request, 'user_messages/message_list.html', {
        'messages': messages,
        'unread_count': unread_count
    })

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('message_list')
    else:
        form = MessageForm()
    return render(request, 'user_messages/send_message.html', {'form': form})
