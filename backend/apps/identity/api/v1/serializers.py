from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)


class LoginSerializer(TokenObtainPairSerializer):
    """
    JWT login serializer.
    """

    username_field = "email"


class RefreshTokenSerializer(TokenRefreshSerializer):
    """
    JWT refresh serializer.
    """

    pass