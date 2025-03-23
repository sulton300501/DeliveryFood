from unidecode import unidecode

from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _

from .fields import ActiveField
from .managers import ActiveManager


class BaseModel(models.Model):
    created_at = models.DateTimeField(_("Kiritilgan sana"), auto_now_add=True)
    update_at = models.DateTimeField(_("O'zgartrilgan sana"), auto_now=True)

    class Meta:
        abstract = True


class Slugify(models.Model):
    slug = models.SlugField(_("slug"), max_length=255, null=True, blank=True, unique=True)
    SLUG_FORM_FIELD = None

    class Meta:
        abstract = True

    def _make_slug(self, value):
        if value is not None:
            original_slug = slugify(unidecode(value))
            unique_slug = original_slug
            num = 1

            while self.__class__.objects.exclude(pk=self.pk).filter(slug=unique_slug).exists():
                unique_slug = f"{original_slug}-{num}"
                num += 1

            return slugify(unique_slug)

    def save(self, *args, **kwargs):
        if self.slug is None:
            value_for_slug = getattr(self, self.SLUG_FORM_FIELD)
            self.slug = self._make_slug(value_for_slug)
        return super().save(*args, **kwargs)


class MultiLangSlugify(Slugify):
    slug_from_lang = models.CharField(
        choices=settings.MODELTRANSLATION_LANGUAGES_CHOICES,
        max_length=60,
        null=True,
        blank=True,
        verbose_name=_("slug tilini tanlash"),
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.slug_from_lang is not None:
            value_for_slug = getattr(self, f"{self.SLUG_FORM_FIELD}_{self.slug_from_lang}")
            self.slug = self._make_slug(value_for_slug)

        if self.slug is None and self.slug_from_lang is None:
            self.slug_from_lang = get_language()
        return super().save(*args, **kwargs)


class SingletonModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)

    def all_objects(self):
        return models.QuerySet(self.model, using=self.db)


class SingletonModel(models.Model):
    active = ActiveField()
    objects = SingletonModelManager()

    class Meta:
        abstract = True
        unique_together = (("id",),)

    def save(self, *args, **kwargs):
        self.pk = 1
        self.active = True
        super().save(*args, **kwargs)

    @property
    def single_str(self):
        return str(self)

    single_str.fget.short_description = ""  # type: ignore # noqa: F401

    @classmethod
    def get_solo(cls):
        return cls.objects.get_or_create(pk=1)[0]


class ActiveModel(models.Model):
    objects = ActiveManager()
    active = ActiveField()

    class Meta:
        abstract = True
