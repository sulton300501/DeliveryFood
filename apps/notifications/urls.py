from django.urls import path

from .views import MessageListCreateView, RoomListCreateView

urlpatterns = [
    path("chat/rooms/", RoomListCreateView.as_view(), name="room-list-create"),
    path("chat/messages/", MessageListCreateView.as_view(), name="message-list-create"),
]
