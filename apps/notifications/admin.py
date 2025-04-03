from django.contrib import admin

from apps.notifications.models import Message, Room

# Register your models here.


admin.site.register(Room)
admin.site.register(Message)
