import re

import pytest
from rest_framework.exceptions import ValidationError

from django.utils import timezone

from apps.common.utils import custom_exception_handler, generate_upload_path


class DummyInstance:
    class _meta:
        app_label = "testapp"
        model_name = "testmodel"


@pytest.mark.django_db
def test_generate_upload_path_format():
    instance = DummyInstance()
    filename = "example_file.jpg"
    result = generate_upload_path(instance, filename)

    # Sana formatini tekshiramiz (sani timezone formatga moslab chiqariladi)
    now_str = timezone.now().strftime("%Y-%m-%d")
    # Regex pattern
    pattern = rf"^testapptestmodelexample_file-{now_str} \d{{2}}:\d{{2}}:\d{{2}}\.jpg$"

    assert re.match(pattern, result), f"Path '{result}' does not match pattern '{pattern}'"


@pytest.mark.django_db
def test_custom_exception_handler_with_validation_error():
    exc = ValidationError({"field": ["This field is required"]})
    context = {}

    response = custom_exception_handler(exc, context)

    assert response is not None
    assert response.status_code == 400
    assert "status_code" in response.data
    assert "errors" in response.data
    assert isinstance(response.data["errors"], list)
    assert response.data["errors"][0]["error"] == "invalid"
    assert response.data["errors"][0]["message"] == "This field is required"
