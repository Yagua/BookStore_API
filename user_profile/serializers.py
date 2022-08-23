from rest_framework import serializers

from core.models import UserProfile
from user.serializers import UserSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = (
            "user",
            "picture",
            "adress_line_1",
            "adress_line_2",
            "city",
            "state_provice_region",
            "zip_code",
            "phone",
            "country",
        )
