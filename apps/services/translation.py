from modeltranslation.translator import TranslationOptions, register

from apps.services.models import Topping


@register(Topping)
class ToppingTranslationOption(TranslationOptions):
    fields = ("name",)
