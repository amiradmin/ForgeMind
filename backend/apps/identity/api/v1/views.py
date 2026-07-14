from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


class LoginView(TokenObtainPairView):
    """
    Obtain JWT access and refresh tokens.
    """

    @extend_schema(
        tags=["Authentication"],
        summary="Login",
        description="Obtain JWT access and refresh tokens.",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class RefreshTokenView(TokenRefreshView):
    """
    Refresh JWT access token.
    """

    @extend_schema(
        tags=["Authentication"],
        summary="Refresh token",
        description="Refresh JWT access token using refresh token.",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
