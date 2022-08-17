from rest_framework import serializers
from core.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "first_name",
            "second_name",
            "paternal_last_name",
            "maternal_last_name",
            "is_active",
            "is_staff",
            "picture",
        )
        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 5
            },
            "picture": {
                "required": False
            },
            "is_active": {
                "required": False
            },
            "is_staff": {
                "required": False
            },
        }
