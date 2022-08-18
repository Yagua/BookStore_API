from rest_framework import serializers
from core.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
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
                "required": False,
                "read_only": True
            },
        }

    def create(self, validated_data):
        """
        Create a new user with the validated data
        """

        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        """
        Update an existing user
        """

        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get(
            "first_name", instance.first_name
        )
        instance.second_name = validated_data.get(
            "second_name", instance.second_name
        )
        instance.paternal_last_name = validated_data.get(
            "paternal_last_name", instance.paternal_last_name
        )
        instance.maternal_last_name = validated_data.get(
            "maternal_last_name", instance.maternal_last_name
        )
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.is_staff = validated_data.get("is_staff", instance.is_staff)
        instance.picture = validated_data.get("picture", instance.picture)

        password = validated_data.get("password", None)
        if password:
            instance.set_password(password)

        instance.save()
        return instance
