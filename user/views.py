from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


class CreateListUserAPI(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #  define how the raw data in the request should be
    #  processed into a Python-native format that can be used in the view.
    parser_classes = [MultiPartParser,FormParser]

    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

    def list(self,request):
        users = self.queryset.all()
        serializer = self.get_serializer(users,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

 