from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Message

@login_required
def index(request):
    return render(request, 'chatapp/index.html')

@login_required
def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)[0:25]

    return render(request, 'chatapp/room.html', {'room_name': room_name, 'username': username, 'messages': messages})