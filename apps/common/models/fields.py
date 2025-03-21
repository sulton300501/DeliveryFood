# from django.db.models import CharField , BooleanField , IntegerField
# from django.utils.translation import gettext_lazy as _
# from apps.common.validators import phone_validators
# from django.core.validators import MinValueValidator




# class ActiveField(BooleanField):
#     def __init__(self, verbose_name=_("active"), default=False, **kwargs):
#         super().__init__(verbose_name=verbose_name , default=default, **kwargs)




# class PhoneField(CharField):
#     def __init__(self, verbose_name=_("telefon raqam") , max_length=15 , validators=None, **kwargs):
#         if validators is None:
#             validators = [phone_validators]
#         super().__init__(verbose_name=verbose_name ,max_length=max_length , validators=validators, **kwargs)


# class OrderField(IntegerField):
#     def __init__(self, verbose_name=_("tartib raqam") , default=1 , validators=None , **kwargs):
#         if validators is None:
#             validators = [MinValueValidator(1)]
#         super().__init__(self , verbose_name=verbose_name , default=default  , validators=validators, **kwargs)
