from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer
from core.models import User

@api_view(["GET"])
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
