from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserProfileSerializer
from core.models import UserProfile


@api_view(["GET"])
def get_user_profile(request):
    """
    Get profile of the current user
    """
    try:
        user = request.user
        user_profile = UserProfile.objects.get(user=user)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "Something went wrong retriving user profile",
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PATCH"])
def update_user_profile(request):
    """
    Update current user profile
    """

    user = request.user
    data = request.data
    user_profile = UserProfile.objects.get(user=user)
    serializer = UserProfileSerializer(user_profile, data=data, partial=True)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
