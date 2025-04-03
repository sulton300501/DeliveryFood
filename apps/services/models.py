from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models.base import BaseModel

# Create your models here.


class Size(BaseModel):
    class SIZE_CHOICES(models.TextChoices):
        SMALL = "S", _("s")
        MEDIUM = "M", _("m")
        LARGE = "L", _("l")
        EXTRA_LARGE = "XL", _("xl")

    code = models.CharField(max_length=2, choices=SIZE_CHOICES, default=SIZE_CHOICES.MEDIUM)
    price_adjustment = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Narxni oshirish yoki kamaytirish uchun qiymat"
    )

    class Meta:
        verbose_name = _("Ovqat o'lchami")
        verbose_name_plural = _("1. Ovqat o'lchamlari")

    def __str__(self):
        return self.code


class Topping(BaseModel):
    name = models.CharField(max_length=50, verbose_name="Topping nomi")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Topping narxi")

    class Meta:
        verbose_name = "Qo'shimcha"
        verbose_name_plural = "Qo'shimchalar"

    def __str__(self):
        return self.name


class OrderDetails(BaseModel):
    order = models.ForeignKey(
        "Order", on_delete=models.CASCADE, verbose_name=_("Buyurtmalar"), related_name="orderdetails"
    )
    food = models.ForeignKey("main.Food", on_delete=models.CASCADE, verbose_name=_("Ovqatlar"))
    size = models.ForeignKey("Size", on_delete=models.CASCADE, verbose_name=_("O'lchami"))
    topping = models.ForeignKey("Topping", on_delete=models.CASCADE, verbose_name=_("Qoshimchalar"))
    quantity = models.IntegerField(_("Miqdori"))
    price = models.DecimalField(_("Narxi"), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _("Buyurtma tafsiloti")
        verbose_name_plural = _("Buyurtma tafsilotlari")

    def __str__(self):
        return f"{self.food} - {self.quantity} dona"


class Order(BaseModel):
    class PaymentMethod(models.TextChoices):
        CASH = "cash", _("Naqd")
        CARD = "card", _("Plastik")

    class Status(models.TextChoices):
        PENDING = "pending", _("Kutilmoqda")
        CONFIRMED = "confirmed", _("Tasdiqlandi")
        DELIVERED = "delivered", _("Yetkazildi")
        CANCELLED = "cancelled", _("Bekor qilindi")

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name=_("Foydalanuvchi"))
    restourant = models.ForeignKey("aboutus.Restourant", on_delete=models.CASCADE, verbose_name=_("orderrestourant"))
    total_price = models.DecimalField(_("Umumiy narx"), max_digits=10, decimal_places=2)
    notes = RichTextUploadingField(_("Kommentariya"))
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING, verbose_name=_("Holati"))
    payment_method = models.CharField(
        max_length=20, choices=PaymentMethod.choices, default=PaymentMethod.CASH, verbose_name=_("To'lov usuli")
    )

    class Meta:
        verbose_name = _("Buyurtma")
        verbose_name_plural = _("Buyurtmalar")

    def __str__(self):
        return f"Buyurtma #{self.id} - {self.user}"
