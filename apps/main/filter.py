from django_filters import Filter, FilterSet

from apps.main.models import Food


class M2MFilter(Filter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def filter(self, qs, value):
        if not value:
            return qs
        values = value.split(",")
        values = [int(v) for v in value]

        qs = qs.filter(tags__id__in=values)
        return qs


class FoodFilter(FilterSet):
    tags = M2MFilter()

    class Meta:
        model = Food
        fields = ("tags",)
