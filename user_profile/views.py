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

@api_view(["PUT"])
def update_user_profile(request):
    """
    Update current user profile
    """

    try:
        user = request.user
        data = request.data
        user_profile = UserProfile.objects.get(user=user)

        user_profile.picture = data.get("picture", user_profile.picture)
        user_profile.adress_line_1 = data.get(
            "adress_line_1", user_profile.adress_line_1
        )
        user_profile.adress_line_2 = data.get(
            "adress_line_2", user_profile.adress_line_2
        )
        user_profile.city = data.get("city", user_profile.city)
        user_profile.state_provice_region = data.get(
            "state_provice_region", user_profile.state_provice_region
        )
        user_profile.zip_code = data.get("zip_code", user_profile.zip_code)
        user_profile.phone = data.get("phone", user_profile.phone)
        user_profile.country = data.get("country", user_profile.country)
        user_profile.save()

        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "message": "Something went wrong updating user profile",
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
