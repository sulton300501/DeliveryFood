from unittest.mock import MagicMock, patch

import pytest
from rest_framework.test import APIRequestFactory

from apps.common.serializers import ThumbnailImageSerializer


@pytest.fixture
def fake_image():
    # Soxta rasm fayli
    mock_image = MagicMock()
    mock_image.name = "test.jpg"
    return mock_image


@pytest.fixture
def fake_request():
    factory = APIRequestFactory()
    return factory.get("/some-url/")


@patch("apps.common.serializers.get_image_dimensions")
@patch("apps.common.serializers.get_thumbnail")
def test_thumbnail_image_serializer(mock_get_thumbnail, mock_get_dimensions, fake_image, fake_request):
    # Rasm o'lchamlari soxta qiymat
    mock_get_dimensions.return_value = (600, 400)

    # Har bir thumbnail uchun soxta natija
    mock_get_thumbnail.side_effect = lambda img, size, quality=99: MagicMock(url=f"/media/thumbs/{size}.jpg")

    serializer = ThumbnailImageSerializer(context={"request": fake_request})
    result = serializer.to_representation(fake_image)

    assert result["large"].endswith("/media/thumbs/400x266.jpg")
    assert result["medium"].endswith("/media/thumbs/300x200.jpg")
    assert result["small"].endswith("/media/thumbs/200x133.jpg")

    # Tekshiruvlar
    mock_get_dimensions.assert_called_once_with(fake_image)
    assert mock_get_thumbnail.call_count == 3
