from image_uploader_widget.widgets import ImageUploaderWidget

from django.db.models import ImageField


class ImageFieldMixin:
    formfield_overrides = {ImageField: {"widget": ImageUploaderWidget}}
