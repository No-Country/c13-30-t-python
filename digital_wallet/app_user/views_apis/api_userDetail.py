from ..serializer import CreateUserDetailSerializer
from ..models import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


# class UserDetailApiView(APIView):


class CreateUserDetail(APIView):

    # def get(self, request):
    #     user_detail = User.objects.all()
    #     serializer = UserDetailSerializer(user_detail, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        serializer = CreateUserDetailSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            validatedData = serializer.validated_data
            serializer.create(validatedData)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
