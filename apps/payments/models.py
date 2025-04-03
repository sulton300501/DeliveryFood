import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class UserCard(models.Model):
    class ProviderChoices(models.TextChoices):
        MASTER = "master", "Master"
        HUMO = "humo", "Humo"
        UZCARD = "uzcard", "Uzcard"
        VISA = "visa", "Visa"

    cardId = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name="usercards")
    provider = models.CharField(choices=ProviderChoices.choices, max_length=16)
    card_number = models.CharField(max_length=16)
    expire_date = models.CharField(max_length=4)
    cvv = models.CharField(max_length=10, null=True, blank=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    token = models.UUIDField(null=True)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.card_number = f"{self.card_number}_deleted_{self.cardId}"
        self.save()

    class Meta:
        verbose_name = _("UserCard")
        verbose_name_plural = _("1. Usercards")
        unique_together = ("user", "card_number")


class Transaction(models.Model):
    class PaymentTypeChoice(models.TextChoices):
        CASH = "cash", _("Naqd")
        CARD = "card", _("Karta")

    class TransactionStatusChoices(models.TextChoices):
        PENDING = "pending", _("Yangi")
        PAID = "paid", _("To'langan")
        CANCELED = "cancelled", _("Bekor qilindi")
        FAILED = "failed", _("Amalga oshirilmadi")

    user = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name="transactions")
    payment_type = models.CharField(choices=PaymentTypeChoice.choices, max_length=16)
    card = models.ForeignKey(UserCard, on_delete=models.PROTECT, null=True, blank=True, related_name="transactions")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    order = models.ForeignKey("services.Order", on_delete=models.PROTECT, related_name="transactions")
    created_at = models.DateField(auto_now=True)
    logs = models.TextField(null=True, blank=True)
    status = models.CharField(
        choices=TransactionStatusChoices.choices, default=TransactionStatusChoices.PENDING, max_length=50
    )
    withdrawed = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("2. Transactions")


class PaymentRefund(models.Model):
    class PaymentRefundStatusChoices(models.TextChoices):
        PENDING = "pending", _("Yangi")
        APPROVED = "approved", _("Qabul qilindi")
        CANCELED = "cancelled", _("Bekor qilindi")
        FAILED = "failed", _("Amalga oshmadi")

    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT, related_name="payment_refunds")
    user = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name="payment_refunds")
    status = models.CharField(
        choices=PaymentRefundStatusChoices.choices, default=PaymentRefundStatusChoices.PENDING, max_length=50
    )
    card = models.ForeignKey(UserCard, on_delete=models.PROTECT, null=True, blank=True, related_name="payment_refunds")

    class Meta:
        verbose_name = _("PaymentRefund")
        verbose_name_plural = _("3. PaymentRefunds")


class Withdrawal(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    teacher = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name="withdrawals")
    card = models.ForeignKey(UserCard, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = _("Withdrawal")
        verbose_name_plural = _("4. Withdrawals")
