from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Room(models.Model):
    room_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("Xona nomi")
        verbose_name_plural = _("1. Xona nomlari")

    def __str__(self):
        return self.room_name


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="message")
    sender = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name = _("Xabar")
        verbose_name_plural = _("2. Xabarlar")

    def __str__(self):
        return f"{self.room}"
