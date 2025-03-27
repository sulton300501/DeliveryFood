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


class CategoryRestourant(MultiLangSlugify, BaseModel):
    name = models.CharField(_("Kategoriyasi"), max_length=256)
    image = ImageField(_("Rasm"), null=True, blank=True)
    order = OrderField()
    SLUG_FORM_FIELD = "name"  # type: ignore # noqa: F401

    class Meta:
        verbose_name = _("Kategoriya")
        verbose_name_plural = _("1. Kategoriyalar")

    def __str__(self):
        return self.name


class MediaFile(BaseModel, ActiveModel):
    title = models.CharField(verbose_name=_("hujjat nomi"), max_length=512)
    file = models.FileField(verbose_name=_("hujjat"), upload_to=generate_upload_path)
    type = models.CharField(max_length=6)
    file_size = models.FloatField(verbose_name=_("hujjat hajmi"), default=0)
    order = OrderField()

    def clean(self):
        self.file_size = self.file.size
        t = self.file.path
        t = t.split(".")
        self.type = t[-1]
        return self

    @property
    def get_file(self):
        if self.file:
            return f"{settings.HOST}{self.file.url}"

    @property
    def short_title(self):
        return truncatechars(self.title, 30)

    short_title.fget.short_description = _("sarlavha")  # type: ignore # noqa: F401

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("order",)
        verbose_name = _("Hujjar")
        verbose_name_plural = _("2. Hujjatlar")


class Food(BaseModel):
    pass


class FoodReviews(BaseModel):
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
    food = models.ForeignKey(
        "Food",
        on_delete=models.CASCADE,
        verbose_name=_("Ovqat"),
        related_name="restourant",
    )

    class Meta:
        verbose_name = _("Fikr-mulohaza")
        verbose_name_plural = _("2. Fikr-mulohazalar")
