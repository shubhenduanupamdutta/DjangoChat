from django.shortcuts import render
from .models import ChatRoom


# Create your views here.
def index(request):
    chat_rooms = ChatRoom.objects.all()
    return render(request, 'chat/index.html', {"chat_rooms": chat_rooms})


def chat_room(request, slug):
    chat_room = ChatRoom.objects.get(slug=slug)
    return render(request, 'chat/room.html', {"chat_room": chat_room})
