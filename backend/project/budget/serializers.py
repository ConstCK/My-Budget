from abc import ABC

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
    category_title = serializers.CharField()

    class Meta:
        fields = "__all__"
        model = Spending


class IncomeSerializer(serializers.ModelSerializer):
    category_title = serializers.CharField()
    class Meta:
        fields = "__all__"
        model = Income


class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = IncomeCategory


class SpendingCategorySerializer(serializers.ModelSerializer):
    sum = serializers.IntegerField(read_only=True)

    class Meta:
        fields = "__all__"
        model = IncomeCategory


class PlanSerializer(serializers.ModelSerializer):
    category_info = SpendingCategorySerializer(read_only=True, source='category')

    class Meta:
        fields = "__all__"
        model = SpendingPlan


class GeneralStatisticSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    overall = serializers.IntegerField(min_value=0, default=0, read_only=True)
    planned = serializers.IntegerField(read_only=True, default=0, )
    title = serializers.CharField(max_length=128, read_only=True)
