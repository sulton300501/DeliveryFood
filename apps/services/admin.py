from django.contrib import admin  # noqa
from django.utils.translation import gettext_lazy as _

from apps.services.models import Order, OrderDetails, Size, Topping
from core.settings.base import MODELTRANSLATION_LANGUAGES


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    model = Size
    list_display = ("id", "code", "price_adjustment")
    search_fields = ("id",)
    list_filter = ("id",)
    ordering = ("id",)
    list_display_links = ("id", "code", "price_adjustment")

    fieldsets = ((_("Qoshimcha"), {"fields": ("code", "price_adjustment")}),)

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    model = Topping
    list_display = ("id", "name", "price")
    search_fields = ("id", "name_uz", "name_ru")
    list_filter = ("id",)
    ordering = ("id",)
    list_display_links = ("id", "name", "price")

    fieldsets = (
        (_("O'zbekcha uz"), {"fields": ("name_uz",)}),
        (_("Ruscha ru"), {"fields": ("name_ru",)}),
        (_("Qoshimcha"), {"fields": ("price",)}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    model = OrderDetails
    list_display = ("id", "quantity", "price")
    search_fields = ("id",)
    list_filter = ("id",)
    ordering = ("id",)
    list_display_links = ("id", "quantity", "price")

    fieldsets = ((_("Qoshimcha"), {"fields": ("order", "food", "size", "topping", "quantity", "price")}),)

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ("id", "total_price", "status")
    search_fields = ("id",)
    list_filter = ("id",)
    ordering = ("id",)
    list_display_links = ("id", "total_price", "status")

    fieldsets = (
        (_("Qoshimcha"), {"fields": ("user", "restourant", "total_price", "notes", "status", "payment_method")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form
