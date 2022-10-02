from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CustomTokenObteinPairView
from user_profile.serializers import UserProfileSerializer

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObteinPairView

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({
                "error": "user identified with the given credentials not found"
            }, status=status.HTTP_404_NOT_FOUND)

        login_serializer = self.serializer_class(data=request.data)
        if not login_serializer.is_valid():
            return Response(
                login_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        user_profile_serializer = UserProfileSerializer(user.profile)
        return Response({
            "profile": user_profile_serializer.data,
            "tokens": login_serializer.validated_data
        }, status=status.HTTP_200_OK)
