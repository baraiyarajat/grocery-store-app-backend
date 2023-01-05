from django.shortcuts import render
from rest_framework.views import APIView
from accounts.models import Account
from .models import Wallet
from .serializers import WalletSerializer
from rest_framework.response import Response
from accounts.authentication import JWTAuthentication
from django.core.exceptions import ObjectDoesNotExist

class WalletDetailsView(APIView):
    authentication_classes = [JWTAuthentication, ]
    def get(self, request, user_id):
        try:
            wallet_object = Wallet.objects.get(user__id=user_id)
            wallet_serializer = WalletSerializer(wallet_object)
            return Response(wallet_serializer.data, status=200)
        except ObjectDoesNotExist:
            print('Creating new Wallet')
            user = Account.objects.get(id=user_id)
            wallet_object = Wallet.objects.create(user=user)
            wallet_serializer = WalletSerializer(wallet_object)
            return Response(wallet_serializer.data, status=200)
        except Exception as e:
            print(e)
            return Response(status=500)


class AddCreditToWallet(APIView):

    def patch(self, request):
        try:
            user_id = request.data['user_id']
            credit_amount = request.data['card_details']['credit_amount']

            # Credit Card Validations

            # Wallet Update
            wallet_object = Wallet.objects.get(user__id=user_id)
            wallet_object.credit += int(credit_amount)
            wallet_object.save()
            return Response(status=200)
        except Exception as e:
            print(e)
            return Response(status=500)


class DebitAmountFromWallet(APIView):

    def patch(self, request):
        try:
            user_id = request.data['user_id']
            credit_amount = request.data['debit_amount']

            # Credit Card Validations

            # Wallet Update
            wallet_object = Wallet.objects.get(user__id=user_id)
            wallet_object.credit -= credit_amount
            wallet_object.save()
            return Response(status=200)
        except Exception as e:
            print(e)
            return Response(status=500)