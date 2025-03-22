from django.db import models


class ActiveQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)


class ActiveManager(models.Manager.from_queryset(ActiveQuerySet)):  # type: ignore # noqa F401
    pass
