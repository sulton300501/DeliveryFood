import pytest
from rest_framework import status

from apps.aboutus.tasks import send_reviews_task


@pytest.mark.django_db
def test_send_reviews(reviews, user):
    id = reviews.id
    user_id = user.id
    message = reviews.comment
    from_email = "sultonmalik@gmail.com"
    recipient_list = "maliksulton@gmail.com"

    response = send_reviews_task(
        id=id, user=user_id, message=message, from_email=from_email, recipient_list=recipient_list
    )

    assert response["status_code"] == status.HTTP_200_OK
