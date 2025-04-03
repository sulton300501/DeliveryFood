from rest_framework import generics

from django.shortcuts import render  # noqa

from .models import Message, Room
from .serializers import MessageSerializer, RoomSerializer

# Create your views here.


# from django.shortcuts import render
# from .models import *

# # Create your views here.


# def CreateRoom(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         room = request.POST["room"]

#         try:
#             get_room = Room.objects.get(room_name=room)
#         except Room.DoesNotExist:
#             new_room = Room(room_name=room)
#             new_room.save()


class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
