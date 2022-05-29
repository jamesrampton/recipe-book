from django.contrib.auth import authenticate, login, logout
from recipes.api_v1.views.base import BurstRateThrottle
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class LoginView(APIView):

    permission_classes = [
        AllowAny,
    ]
    throttle_classes = [
        BurstRateThrottle,
    ]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if not user or user.is_anonymous:
            return Response(
                {'detail': 'Unable to login with provided credentials'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        elif not user.is_active:
            return Response(
                {'detail': 'User is inactive'}, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            auth_token, _ = Token.objects.get_or_create(user=user)
            login(request, user)
            login_data = {
                'auth_token': auth_token.key,
            }
        return Response(login_data)


class LogoutView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]
    throttle_classes = [
        BurstRateThrottle,
    ]

    def post(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()
        except:
            pass
        logout(request)

        return Response(
            {'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK
        )
