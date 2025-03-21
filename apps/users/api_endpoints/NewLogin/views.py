# from rest_framework.generics import GenericAPIView
# from .serializers import NewLoginSerializer
# from rest_framework.response import Response
# from rest_framework import status




# class NewLoginAPIView(GenericAPIView):
#     serializer_class = NewLoginSerializer

#     def post(self , request , *args , **kwargs):
#         data = self.serializer_class(data=request.data)
#         if data.is_valid():
#             response = data.save()
#             return Response(response)
#         return Response(data.errors , status=status.HTTP_400_BAD_REQUEST)


# __all__ = ["NewLoginAPIView"]
