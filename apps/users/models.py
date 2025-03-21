# from django.db import models
# from django.utils.translation import gettext_lazy as _
# from apps.common.models.fields import PhoneField
# from apps.common.models.base import BaseModel , ActiveModel
# from apps.common.models.model import Address
# from sorl.thumbnail import ImageField
# from apps.common.utils import generate_upload_path
# from django.contrib.auth.models import AbstractUser
# from django.conf import settings


# # Create your models here.


# class User(AbstractUser , BaseModel , ActiveModel):
#     class GenderChoice(models.TextChoices):
#         MALE = "Male" , _("Erkak")
#         FEMALE = "Female" , _("Ayol")


#     full_name = models.CharField(_("Toliq ism") , max_length=255 , null=True , blank=True)
#     phone_number = PhoneField(verbose_name=_("Foydalanuvchi raqami"))
#     email = models.EmailField(verbose_name=_("Email pochta") , max_length=40 , null=False , blank=False )
#     address_id = models.ForeignKey(Address , on_delete=models.CASCADE , verbose_name=_("Yashash manzili"))
#     avatar = ImageField(verbose_name=_("Rasm") ,upload_to=generate_upload_path)
#     birthdate = models.DateTimeField(_("Tugilgan sana") , null=True , blank=True)
#     gender = models.CharField(_("Jinsi") , choices=GenderChoice.choices , max_length=255)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)

#     @property
#     def get_avatar(self):
#         if self.avatar:
#             return f"{settings.HOST}{self.avatar.url}"

#     class Meta:
#         verbose_name = _("Foydalanuvchilar")
#         verbose_name_plural = _("Foydalanuvchilar")
