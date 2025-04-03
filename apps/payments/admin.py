from django.contrib import admin

from .models import PaymentRefund, Transaction, UserCard, Withdrawal

# Register your models here.


admin.site.register(UserCard)
admin.site.register(Transaction)
admin.site.register(PaymentRefund)
admin.site.register(Withdrawal)
