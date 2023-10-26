from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from budget.models import Balance, Spending, Income, IncomeCategory, SpendingPlan


class UserSerializer(serializers.ModelSerializer):

    def validate_password(self, value):
        validate_password(value)
        return value

    class Meta:
        fields = ["username", "password"]
        model = User
        extra_kwargs = {'password': {"write_only": True}}


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


class PlanSerializer(serializers.ModelSerializer):
    category_info = SpendingCategorySerializer(read_only=True, source='category')

    class Meta:
        fields = "__all__"
        model = SpendingPlan
