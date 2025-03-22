# from common.models.model import City
# from django_filters import Filter, FilterSet


# class M2MFilter(Filter):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def filter(self, qs, value):
#         if not value:
#             return qs
#         values = value.split(",")
#         values = [int(v) for v in value]

#         qs = qs.filter(tags__id__in=values)
#         return qs


# class FaqFilter(FilterSet):
#     tags = M2MFilter()

#     class Meta:
#         model = City
#         fields = ("tags",)
