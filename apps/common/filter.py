# from django_filters import Filter , FilterSet
# from common.models import models




# class M2MFilter(Filter):
#     def __init__(self , *args , **kwargs):
#         super().__init__( *args , **kwargs)


#     def filter(self , qs , value):
#         if not value:
#             return qs
#         values = value.split(",")
#         values = [int(v) for v in value]

#         qs = qs.filter(tags__id__in=values)
#         return qs


# class FaqFilter(M2MFilter):
#     tags = M2MFilter()

#     class Meta:
#         model = models
#         fields = ("tags",)
