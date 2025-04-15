from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from .serializers import ProfileSerializer


class ProfileAPIView(GenericAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (FormParser, MultiPartParser)

    @swagger_auto_schema(tags=["users"])
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @swagger_auto_schema(tags=["users"])
    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(instance=user, data=request.data, partial=True)

        if serializer.is_valid():
            response = serializer.save()
            return Response(response.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=["users"])
    def delete(self, request, *args, **kwargs):
        request.user.delete()
        return Response({"message": "User profile deleted successfully"})

    @swagger_auto_schema(tags=["users"])
    def put(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(instance=user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


__all__ = ["ProfileAPIView"]
