
# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'chatter_21720/index.html', {})

def room(request, room_name):
    return render(request, 'chatter_21720/room.html', {
        'room_name': room_name
    })
