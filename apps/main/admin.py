from django.contrib import admin  # noqa
from django.utils.translation import gettext_lazy as _

from apps.common.mixins import ImageFieldMixin
from apps.main.models import CategoryFood, Food, FoodReviews, MediaFile, Promo, Tags
from core.settings.base import MODELTRANSLATION_LANGUAGES

# Register your models here.


# Register your models here.
@admin.register(CategoryFood)
class CategoryAdmin(ImageFieldMixin, admin.ModelAdmin):
    model = CategoryFood
    list_display = ("id", "name", "order")
    search_fields = ("name_uz", "name_ru")
    list_filter = ("id",)
    ordering = ("id",)
    list_display_links = ("id", "name")

    fieldsets = (
        (_("O'zbekcha uz"), {"fields": ("name_uz",)}),
        (_("Ruscha ru"), {"fields": ("name_ru",)}),
        (_("Qoshimcha"), {"fields": ("image", "order", "slug_from_lang")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


# Register your models here.
@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    model = MediaFile
    list_display = ("id", "title", "file_size", "order")
    search_fields = ("title_uz", "title_ru")
    list_filter = ("id",)
    ordering = ("id",)
    list_display_links = ("id", "title")
    readonly_fields = ("type", "file_size")

    fieldsets = (
        (_("O'zbekcha uz"), {"fields": ("title_uz",)}),
        (_("Ruscha ru"), {"fields": ("title_ru",)}),
        (_("Qoshimcha"), {"fields": ("food", "file", "type", "file_size", "order")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    model = Tags
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


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    model = Promo
    list_display = ("id", "name")
    search_fields = ("name_uz", "name_ru")
    list_filter = ("id",)
    ordering = ("id",)
    list_display_links = ("id", "name")

    fieldsets = (
        (_("O'zbekcha uz"), {"fields": ("name_uz",)}),
        (_("Ruscha ru"), {"fields": ("name_ru",)}),
        (_("Qoshimcha"), {"fields": ("discount_percent", "start_date", "end_date")}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    model = Food
    list_display = ("id", "name")
    search_fields = ("name_uz", "name_ru")
    list_filter = ("id",)
    ordering = ("id",)
    list_display_links = ("id", "name")

    fieldsets = (
        (_("O'zbekcha uz"), {"fields": ("name_uz", "description_uz")}),
        (_("Ruscha ru"), {"fields": ("name_ru", "description_ru")}),
        (
            _("Qoshimcha"),
            {
                "fields": (
                    "category",
                    "restourant",
                    "base_price",
                    "promo",
                    "is_promo_active",
                    "is_available",
                    "slug_from_lang",
                )
            },
        ),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form


@admin.register(FoodReviews)
class FoodReviewsAdmin(admin.ModelAdmin):
    model = FoodReviews
    list_display = ("id", "rating")
    search_fields = ("id",)
    list_filter = ("id",)
    ordering = ("id",)
    list_display_links = ("id",)

    fieldsets = [
        (_("Qoshimcha"), {"fields": ["rating", "comment", "user", "food"]}),
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in MODELTRANSLATION_LANGUAGES:
                form.base_fields[value].required = True
        return form
