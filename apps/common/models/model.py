# from django.db import models
# from django.utils.translation import gettext_lazy as _
# from apps.common.models.fields import PhoneField
# from apps.common.models.base import BaseModel


# # common -  feedback ,


# class City(BaseModel):
#     name = models.CharField(_("Shahar nomi") , max_length=256)

#     class Meta:
#         verbose_name = _("Shahar")
#         verbose_name_plural = _("1. Shaharlar")


#     def __str__(self):
#         return self.name




# class District(BaseModel):
#     name = models.CharField(_("Tuman nomi"), max_length=256)
#     city_id = models.ForeignKey("City", on_delete=models.CASCADE ,  verbose_name=_("Shahar nomi"), max_length=256)

#     class Meta:
#         verbose_name = _("Kocha nomi")
#         verbose_name_plural = _("2. Ko'cha nomlari")

#     def  __str__(self):
#         return self.name








# class Address(BaseModel):
#     name = models.CharField(verbose_name=_("Manzil nomi") , max_length=256)
#     phone_number = PhoneField(_("Asosiy telefon raqam"))
#     city_id = models.ForeignKey("City", verbose_name=("Shahar nomi") , on_delete=models.CASCADE)
#     detail_address = models.CharField(_("Ko'cha nomi") , max_length=256)


#     class Meta:
#         ordering = ("name",)
#         verbose_name = _("Manzil")
#         verbose_name_plural = _("3. Manzillar")
