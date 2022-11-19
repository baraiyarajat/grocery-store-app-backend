from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        required=True,
    )

    last_name = serializers.CharField(
        required=True,
    )

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Account.objects.all())]
    )

    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        account = Account.objects.create_user(first_name=validated_data['first_name'],
                                              last_name=validated_data['last_name'],
                                              email=validated_data['email'],
                                              password=validated_data['password'])
        return account

    class Meta:
        model = Account
        fields = ('id', 'first_name', 'last_name', 'email', 'password')
