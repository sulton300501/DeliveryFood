from modeltranslation.translator import TranslationOptions, register

from apps.common.models import model


@register(model.City)
class CityTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(model.District)
class DistrictTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(model.Address)
class AddressTranslationOptions(TranslationOptions):
    fields = ("name", "detail_address")
