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


class CategoryFood(MultiLangSlugify, BaseModel):
    name = models.CharField(_("Kategoriyasi"), max_length=256)
    image = ImageField(_("Rasm"), null=True, blank=True)
    order = OrderField()
    SLUG_FORM_FIELD = "name"  # type: ignore # noqa: F401

    @property
    def get_image(self):
        if self.image:
            return f"{settings.HOST}{self.image.url}"

    class Meta:
        verbose_name = _("Kategoriya")
        verbose_name_plural = _("1. Kategoriyalar")

    def __str__(self):
        return self.name


class MediaFile(BaseModel, ActiveModel):
    food = models.ForeignKey(
        "Food", on_delete=models.CASCADE, verbose_name=_("Ovqatlar"), related_name="documents", null=True
    )
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


class Tags(BaseModel):
    name = models.CharField(max_length=512, verbose_name=_("nomi"))

    class Meta:
        verbose_name = _("Ovqatlar tegi")
        verbose_name_plural = _("3. Ovqatlar teglari")

    def __str__(self):
        return self.name

    @property
    def short_name(self):
        return truncatechars(self.name, 30)

    short_name.fget.short_description = _("nomi")  # type: ignore # noqa: F401


class Promo(BaseModel):
    name = models.CharField("Matn", max_length=255, null=True, blank=True)
    discount_percent = models.DecimalField("Promo foizi", max_digits=5, decimal_places=2, null=True, blank=True)
    start_date = models.DateTimeField(_("Boshlanish sanasi"), null=True, blank=True)
    end_date = models.DateTimeField(_("Tugash sanasi"), null=True, blank=True)

    class Meta:
        verbose_name = _("Promo Foiz")
        verbose_name_plural = _("4. Promo Foizlar")

    def __str__(self):
        return self.name

    @property
    def short_name(self):
        return truncatechars(self.name, 30)

    short_name.fget.short_description = _("Promo")  # type: ignore # noqa: F401


class Food(BaseModel, MultiLangSlugify):
    name = models.CharField(_("Ovqat nomi"), max_length=255)
    description = models.TextField(_("Ovqat tavsifi"), null=True, blank=True)
    category = models.ForeignKey(
        "CategoryFood", on_delete=models.CASCADE, verbose_name=_("Ovqat Kategorysi"), related_name="food"
    )
    restourant = models.ForeignKey("aboutus.Restourant", on_delete=models.CASCADE, verbose_name=_("restaurant_food"))
    base_price = models.CharField(_("Asosiy narx"), max_length=55)
    promo = models.ManyToManyField("Promo", verbose_name=_("Promo"), blank=True)
    is_promo_active = models.BooleanField(_("Faol Promo"))
    tags = models.ManyToManyField("Tags", verbose_name=_("Ovqat teglari"))
    is_available = models.BooleanField(_("Ovqat mavjudligi"))
    SLUG_FORM_FIELD = "name"  # type: ignore # noqa: F401

    class Meta:
        verbose_name = _("Ovqat")
        verbose_name_plural = _("5. Ovqatlar")

    def __str__(self):
        return self.name

    @property
    def short_name(self):
        return truncatechars(self.name, 30)

    short_name.fget.short_description = _("Ovqat")  # type: ignore # noqa: F401


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
        verbose_name=_("Foydalanuvchi"),
    )
    food = models.ForeignKey(
        "Food",
        on_delete=models.CASCADE,
        verbose_name=_("Ovqat"),
    )

    class Meta:
        verbose_name = _("Fikr-mulohaza")
        verbose_name_plural = _("6. Fikr-mulohazalar")
