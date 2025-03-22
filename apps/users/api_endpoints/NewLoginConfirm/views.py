from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import NewLoginConfirmSerializers


class NewLoginConfirmAPIView(GenericAPIView):
    serializer_class = NewLoginConfirmSerializers

    @swagger_auto_schema(tags=["users"])
    def post(self, request, *args, **kwargs):
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            response = data.save()
            return Response(response)
        return ValidationError(data.errors, status=status.HTTP_404_NOT_FOUND)


__all__ = ["NewLoginConfirmAPIView"]
