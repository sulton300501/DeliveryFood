from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.aboutus.models import Reviews

User = get_user_model()

import environ

from apps.aboutus.tasks import send_reviews_task

env = environ.Env()
env.read_env(".env")


@receiver(post_save, sender=Reviews)
def send_reviews(sender, instance, **kwargs):
    print("reviews signal ishladi")
    id = instance.id
    user_id = instance.user.id
    message = instance.comment
    from_email = env.str("EMAIL_HOST_USER")
    recipient_list = [user.email for user in User.objects.all()]
    send_reviews_task(id=id, user=user_id, message=message, from_email=from_email, recipient_list=recipient_list)
