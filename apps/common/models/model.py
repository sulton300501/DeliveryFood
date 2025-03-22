from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models.base import BaseModel, MultiLangSlugify
from apps.common.models.fields import PhoneField


# common -  feedback ,
class City(BaseModel, MultiLangSlugify):
    name = models.CharField(_("Shahar nomi"), max_length=256)

    class Meta:
        verbose_name = _("Shahar")
        verbose_name_plural = _("1. Shaharlar")

    def __str__(self):
        return self.name


class District(BaseModel, MultiLangSlugify):
    name = models.CharField(_("Tuman nomi"), max_length=256)
    city = models.ForeignKey("City", on_delete=models.CASCADE, verbose_name=_("Shahar nomi"), max_length=256)

    class Meta:
        verbose_name = _("Tuman nomi")
        verbose_name_plural = _("2. Tuman nomlari")

    def __str__(self):
        return self.name


class Address(BaseModel, MultiLangSlugify):
    name = models.CharField(verbose_name=_("Viloyat"), max_length=256)
    phone_number = PhoneField(_("Asosiy telefon raqam"))
    city = models.ForeignKey("City", verbose_name=("Shahar nomi"), on_delete=models.CASCADE)
    detail_address = models.CharField(_("Ko'cha nomi"), max_length=256)

    class Meta:
        ordering = ("name",)
        verbose_name = _("Manzil")
        verbose_name_plural = _("3. Manzillar")

    def __str__(self):
        return self.name
