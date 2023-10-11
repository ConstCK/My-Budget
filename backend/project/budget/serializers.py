from django.contrib.auth.models import User
from rest_framework import serializers

from budget.models import Balance, Spending, Income, IncomeCategory


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        fields = ["username", "password"]
        model = User


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Balance


class SpendingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Spending


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Income


class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = IncomeCategory


class SpendingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = IncomeCategory
