from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django.shortcuts import get_object_or_404

from .serializers import UserSerializer
from core.models import User

@api_view(["GET"])
@permission_classes([IsAuthenticated, IsAdminUser])
def list_all_users(request):
    """
    Get all users in database
    """

    users = User.objects.all()
    serializers = UserSerializer(users, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([AllowAny])
def create_user(request):
    """
    Create a new user
    """

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    """
    Get an specific user, update, or delete it
    """

    def get(self, request, pk):
        """
        Get an specific user by pk
        """
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        Update an specific user
        """

        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        """
        Update partially an specific user
        """

        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete an user
        """

        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
