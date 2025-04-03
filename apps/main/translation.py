from modeltranslation.translator import TranslationOptions, register

from apps.main.models import CategoryFood, Food, MediaFile, Promo, Tags


@register(CategoryFood)
class CategoryFoodTranslationOption(TranslationOptions):
    fields = ("name",)


@register(MediaFile)
class MediaFileTranslationOption(TranslationOptions):
    fields = ("title",)


@register(Tags)
class TagsTranslationOption(TranslationOptions):
    fields = ("name",)


@register(Promo)
class PromoTranslationOption(TranslationOptions):
    fields = ("name",)


@register(Food)
class FoodTranslationOption(TranslationOptions):
    fields = ("name", "description")
