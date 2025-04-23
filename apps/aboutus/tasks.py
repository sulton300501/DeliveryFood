from smtplib import SMTPRecipientsRefused

import environ
from celery import shared_task
from rest_framework import status

from django.core.mail import send_mail

env = environ.Env()
env.read_env(".env")


@shared_task
def send_reviews_task(id, user, message, from_email, recipient_list):
    post_url = "http://127.0.0.1:8000/admin/aboutus/reviews/"
    my_message = f"""
        <div style="text-align:center !important; width: 80% !important; margin:0 auto !important;">
            <h1 style="font-size: 40px !important; width: 80% !important;">Fikr mulohaza</h1>
            <div style="display: flex; justify-content: flex-end;">
            </div>
            <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">Fikr mulohaza id: {id}</p>
            <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">Foydalanuvchi id: {user}</p>
            <p style="font-size: 20px !important; width: 80% !important; text-align: left !important;">Sharh:  {message}</p>
            <p style="font-size: 20px !important; width: 80% !important; text-align: left !important; margin-top: 30px;">
            <a href="{post_url}" style="font-size: 20px !important; ">{post_url}</a>
           </p>
        </div>
        """

    for recipient in recipient_list:
        try:
            send_mail(
                subject="Yangi sharh qoldirildi",
                message=None,
                html_message=my_message,
                from_email=from_email,
                recipient_list=(recipient,),
            )
        except SMTPRecipientsRefused:
            pass

    return {"status_code": status.HTTP_200_OK}
