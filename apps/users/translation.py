from modeltranslation.translator import TranslationOptions, register

from .models import User


@register(User)
class UserTranslation(TranslationOptions):
    fields = ("full_name",)
