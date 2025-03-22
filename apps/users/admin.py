from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.common.mixins import ImageFieldMixin
from apps.users.models import User
from core.settings.base import MODELTRANSLATION_LANGUAGES

# Register your models here.


@admin.register(User)
class UserAdmin(ImageFieldMixin, admin.ModelAdmin):
    model = User
    list_display = ("id", "full_name", "phone_number")
    search_fields = ("full_name", "phone_number")
    list_filter = ("id",)
    ordering = ("id",)
    list_display_links = ("id", "full_name", "phone_number")
    fieldsets = (
        (_("O'zbekcha uz"), {"fields": ("full_name_uz",)}),
        (_("Ruscha ru"), {"fields": ("full_name_ru",)}),
        (
            None,
            {
                "fields": (
                    "phone_number",
                    "email",
                    "address_id",
                    "avatar",
                    "birthdate",
                    "gender",
                    "is_superuser",
                    "is_staff",
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
