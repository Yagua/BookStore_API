from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom TokenObtainPair serializers
    """

    @classmethod
    def get_token(cls, user):
        """
        Get token with custom claim
        """

        token = super().get_token(user)
        # Add custom claims
        token["username"] = user.username
        return token
