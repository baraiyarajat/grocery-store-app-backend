import datetime
import string
import random

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework import status
from .serializers import AccountSerializer
from .models import Account, UserToken

from .authentication import create_access_token, create_refresh_token, JWTAuthentication, decode_refresh_token


class AccountCreate(APIView):
    """
    Creates the Account.
    """
    def post(self, request, format='json'):

        data = request.data
        if data['password'] != data['confirmPassword']:
            raise exceptions.APIException("Password do not match!")

        serializer = AccountSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            account = serializer.save()
            if account:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        try:

            email = request.data['email']
            password = request.data['password']

            user = Account.objects.get(email=email)

            if user is None:
                raise exceptions.AuthenticationFailed('Invalid Credentials')

            if not user.check_password(password):
                raise exceptions.AuthenticationFailed('Invalid Credentials')

            access_token = create_access_token(user.id)
            refresh_token = create_refresh_token(user.id)

            UserToken.objects.create(user_id=user.id,
                                     token=refresh_token,
                                     expired_at=datetime.datetime.utcnow() + datetime.timedelta(days=7))

            response = Response()

            response.set_cookie(key='refresh_token', value=refresh_token, httponly=True, samesite='None')

            response.data = {
                'token': access_token
            }

            return response

        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication, ]

    def get(self, request):
        return Response(AccountSerializer(request.user).data)


class RefreshAPIView(APIView):

    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        user_id = decode_refresh_token(refresh_token)

        if not UserToken.objects.filter(
                user_id=user_id,
                token=refresh_token,
                expired_at__gt=datetime.datetime.now(tz=datetime.timezone.utc)
        ).exists():
            raise exceptions.AuthenticationFailed('unauthenticated')

        access_token = create_access_token(user_id)
        return Response(access_token)


class LogoutAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        UserToken.objects.filter(token=refresh_token).delete()

        response = Response()
        response.delete_cookie(key='refresh_token')
        response.data = {
            'message': 'success'
        }

        return response



