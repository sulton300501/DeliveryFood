from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.aboutus.models import (
    CategoryRestourant,
    FavouriteRestaurant,
    Restourant,
    Reviews,
)
from apps.common.mixins import ImageFieldMixin
from core.settings.base import MODELTRANSLATION_LANGUAGES


@admin.register(Restourant)
class RestourantAdmin(ImageFieldMixin, admin.ModelAdmin):
    model = Restourant
    list_display = (
        "id",
        "name",
        "orders_count",
        "working_hourse",
        "active",
        "created_at",
        "update_at",
    )
    search_fields = ("name_uz", "name_ru")
    list_filter = ("id",)
    ordering = ("id",)
    list_display_links = ("id", "name")
    readonly_fields = ("latitude", "longitude", "orders_count")

    fieldsets = (
        (
            _("O'zbekcha uz"),
            {"fields": ("name_uz", "description_uz", "slug_from_lang", "slug")},
        ),
        (_("Ruscha ru"), {"fields": ("name_ru", "description_ru")}),
        (
            _("Asosiy"),
            {
                "fields": (
                    "avatar",
                    "cover_image",
                    "category",
                    "address_id",
                    "location_url",
                    "latitude",
                    "longitude",
                    "orders_count",
                    "working_hourse",
                )
            },
        ),
        (_("Qo'shimcha 🖋"), {"fields": ("active",)}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    model = Reviews
    list_display = ("id", "rating", "comment", "created_at", "update_at")
    search_fields = ("id",)
    list_filter = ("id",)
    ordering = ("id",)
    list_display_links = ("id",)

    fieldsets = ((_("Asosiy"), {"fields": ("rating", "comment", "user", "restourant")}),)

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(FavouriteRestaurant)
class FavouriteRestourantAdmin(admin.ModelAdmin):
    model = FavouriteRestaurant
    list_display = ("id",)
    list_filter = ("id",)
    ordering = ("id",)
    list_display_links = ("id",)
    readonly_fields = ("user", "restourant")

    fieldsets = ((_("Bog'lanishlar 🖋"), {"fields": ("user", "restourant")}),)

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(CategoryRestourant)
class CategoryRestourantAdmin(admin.ModelAdmin):
    model = CategoryRestourant
    list_display = ("id", "name", "created_at", "update_at")
    search_fields = ("name_uz", "name_ru")
    list_filter = ("id",)
    ordering = ("id",)
    list_display_links = ("id", "name")

    fieldsets = (
        (_("O'zbekcha uz"), {"fields": ("name_uz", "slug_from_lang", "slug")}),
        (_("Ruscha ru"), {"fields": ("name_ru",)}),
        (_("Qo'shimcha 🖋"), {"fields": ("order",)}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form
