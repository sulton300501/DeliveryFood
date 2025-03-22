from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.common.models.model import Address, City, District
from core.settings.base import MODELTRANSLATION_LANGUAGES


# Register your models here.
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ("id", "name")
    search_fields = ("name_uz", "name_ru")
    list_filter = ("id",)
    ordering = ("id",)
    list_display_links = ("id", "name")

    fieldsets = (
        (_("O'zbekcha uz"), {"fields": ("name_uz",)}),
        (_("Ruscha ru"), {"fields": ("name_ru",)}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    model = District
    list_display = ("id", "name", "city")
    search_fields = ("name_uz",)
    list_filter = ("id",)
    ordering = ("id",)
    list_display_links = ("id", "name")
    fieldsets = (
        (_("O'zbekcha uz"), {"fields": ("name_uz",)}),
        (_("Ruscha ru"), {"fields": ("name_ru",)}),
        (
            None,
            {"fields": ("city",)},
        ),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    model = Address
    list_display = ("id", "name", "phone_number", "city", "detail_address")
    search_fields = ("name_uz",)
    list_filter = ("id",)
    ordering = ("id",)
    list_display_links = ("id", "name", "phone_number")
    fieldsets = (
        (_("O'zbekcha uz"), {"fields": ("name_uz", "detail_address_uz")}),
        (_("Ruscha ru"), {"fields": ("name_ru", "detail_address_ru")}),
        (
            _("Qoshimcha"),
            {"fields": ("phone_number", "city")},
        ),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form
