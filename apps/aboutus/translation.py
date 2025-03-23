from modeltranslation.translator import TranslationOptions, register

from apps.aboutus.models import CategoryRestourant, Restourant


@register(Restourant)
class RestourantTranslationOption(TranslationOptions):
    fields = ("name", "description")


@register(CategoryRestourant)
class CategoryRestourantTranslationOption(TranslationOptions):
    fields = ("name",)
