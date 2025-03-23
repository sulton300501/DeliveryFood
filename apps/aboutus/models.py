from ckeditor_uploader.fields import RichTextUploadingField
from sorl.thumbnail import ImageField

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.translation import gettext_lazy as _

from apps.common.models.base import ActiveModel, BaseModel, MultiLangSlugify
from apps.common.models.fields import OrderField
from apps.common.utils import generate_upload_path


class Restourant(BaseModel, MultiLangSlugify, ActiveModel):
    name = models.CharField(_("Restourant nomi"), max_length=255)
    description = models.TextField(_("Tavsif"))
    category = models.ForeignKey("CategoryRestourant", on_delete=models.CASCADE, verbose_name=_("Category"))
    avatar = ImageField(_("Rasm"), upload_to=generate_upload_path)
    cover_image = ImageField(_("Asosiy rasm"), upload_to=generate_upload_path)
    address_id = models.ForeignKey("common.Address", on_delete=models.CASCADE, verbose_name=_("Manzil"))
    location_url = models.URLField(max_length=300, verbose_name=_("Joylashuvi"))
    latitude = models.CharField(max_length=55, verbose_name=_("kenglik"), blank=True, null=True)
    longitude = models.CharField(max_length=55, verbose_name=_("uzunlik"), blank=True, null=True)
    orders_count = models.IntegerField(_("Buyurtmalar soni"))
    working_hourse = models.CharField(_("Ish vaqti"), max_length=50, help_text="Masalan: 09:00 - 20:00")
    SLUG_FORM_FIELD = "name"  # type: ignore # noqa:F401

    @property
    def get_avatar(self):
        if self.avatar:
            return f"{settings.HOST}{self.avatar.url}"

    @property
    def get_cover_image(self):
        if self.get_cover_image:
            return f"{settings.HOST}{self.cover_image.url}"

    @property
    def short_title(self):
        return truncatechars(self.description, 30)

    short_title.fget.short_description = ""  # type: ignore # noqa: F401

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id",)
        verbose_name = _("Restourant")
        verbose_name_plural = _("1. Restourantlar")


class Reviews(BaseModel):
    rating = models.FloatField(
        _("Reyting"),
        default=0,
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],
    )
    comment = RichTextUploadingField(verbose_name=_("Komentariya"))
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name=_("Foydalanuvchi"),
    )
    restourant = models.ForeignKey(
        "Restourant",
        on_delete=models.CASCADE,
        verbose_name=_("Restoran"),
        related_name="restourant",
    )

    class Meta:
        verbose_name = _("Fikr-mulohaza")
        verbose_name_plural = _("2. Fikr-mulohazalar")


class FavouriteRestaurant(BaseModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name=_("Foydalanuvchi"),
        related_name="favourite",
    )
    restourant = models.ForeignKey(
        "Restourant",
        on_delete=models.CASCADE,
        verbose_name=_("Foydalanuvchi"),
        related_name="favouriteuser",
    )

    class Meta:
        verbose_name = _("Sevimli restoran")
        verbose_name_plural = _("3. Sevimli restoranlar")


class CategoryRestourant(MultiLangSlugify, BaseModel):
    name = models.CharField(_("Kategoriyasi"), max_length=256)
    order = OrderField()
    SLUG_FORM_FIELD = "name"  # type: ignore # noqa: F401

    class Meta:
        verbose_name = _("Kategoriya")
        verbose_name_plural = _("4. Kategoriyalar")
