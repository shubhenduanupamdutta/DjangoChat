from django.shortcuts import render
from .models import ChatMessage, ChatRoom


# Create your views here.
def index(request):
    chat_rooms = ChatRoom.objects.all()
    return render(request, 'chat/index.html', {"chat_rooms": chat_rooms})


def chat_room(request, slug):
    chat_room = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=chat_room)[:30]
    return render(request, 'chat/room.html', {"chat_room": chat_room, "messages": messages})
