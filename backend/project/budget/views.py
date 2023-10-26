import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Spending, Income, IncomeCategory, SpendingCategory, Balance, SpendingPlan
from .serializers import UserSerializer, SpendingSerializer, IncomeSerializer, \
    IncomeCategorySerializer, SpendingCategorySerializer, BalanceSerializer, PlanSerializer


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = User(username=request.data["username"])
        user.set_password(request.data["password"])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'user': serializer.data, 'token': token.key})
    raise Exception("Ошибка регистрации")


class FamilyViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class BalanceViewSet(viewsets.ModelViewSet):
    serializer_class = BalanceSerializer
    queryset = Balance.objects.all()


class SpendingViewSet(viewsets.ModelViewSet):
    serializer_class = SpendingSerializer
    queryset = Spending.objects.all()


class IncomeViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()


class SpendingCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = SpendingCategorySerializer
    queryset = SpendingCategory.objects.all()


class IncomeCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeCategorySerializer
    queryset = IncomeCategory.objects.all()


@api_view(["POST"])
@authentication_classes([TokenAuthentication, ])
@permission_classes([IsAuthenticated])
def get_main_data(request):
    try:
        current_month = datetime.datetime.now().month
        user = User.objects.get(username=request.data["user"])
        balance = Balance.objects.filter(family=user).last().balance
        spending = Spending.objects.filter(family=user, created_at__month=current_month).aggregate(total_spending=Sum(
            "amount", default=0))
        income = Income.objects.filter(family=user, created_at__month=current_month).aggregate(total_income=Sum(
            "amount", default=0))
        return Response({"balance": balance, "spending": spending, "income": income})
    except ObjectDoesNotExist as error:
        raise Exception(f"Отсутствие данных по объекту... {error}")


@api_view(["POST"])
@authentication_classes([TokenAuthentication, ])
@permission_classes([IsAuthenticated])
def get_income_categories(request):
    try:
        user = User.objects.get(username=request.data["user"])
        queryset = IncomeCategory.objects.filter(family=user)
        serializer = IncomeCategorySerializer(queryset, many=True)
        return Response(serializer.data)
    except ObjectDoesNotExist as error:
        raise Exception(f"Отсутствие данных... {error}")


@api_view(["POST"])
@authentication_classes([TokenAuthentication, ])
@permission_classes([IsAuthenticated])
def get_spending_categories(request):
    try:
        user = User.objects.get(username=request.data["user"])
        queryset = SpendingCategory.objects.filter(family=user)
        serializer = SpendingCategorySerializer(queryset, many=True)
        return Response(serializer.data)
    except ObjectDoesNotExist as error:
        raise Exception(f"Отсутствие данных... {error}")


@api_view(["POST"])
@authentication_classes([TokenAuthentication, ])
@permission_classes([IsAuthenticated])
def delete_income_category(request):
    try:
        obj = IncomeCategory.objects.get(id=request.data["id"])
        obj.delete()
        return Response(f"Успешное удаление категории {obj}")
    except ObjectDoesNotExist as error:
        raise Exception(f"Ошибка удаления... {error}")


@api_view(["POST"])
@authentication_classes([TokenAuthentication, ])
@permission_classes([IsAuthenticated])
def delete_spending_category(request):
    try:
        obj = SpendingCategory.objects.get(id=request.data["id"])
        obj.delete()
        return Response(f"Успешное удаление категории {obj}")
    except ObjectDoesNotExist as error:
        raise Exception(f"Ошибка удаления... {error}")


@api_view(["POST"])
@authentication_classes([TokenAuthentication, ])
@permission_classes([IsAuthenticated])
def add_income_category(request):
    try:
        user = User.objects.get(username=request.data["user"])
        obj = IncomeCategory(family=user,
                             title=request.data["title"],
                             description=request.data["description"])
        obj.save()
        serializer = IncomeCategorySerializer(obj)
        return Response(serializer.data)
    except ObjectDoesNotExist as error:
        raise Exception(f"Ошибка добавления... {error}")
    except IntegrityError as error:
        raise Exception(f"Ошибка добавления... {error}")


@api_view(["POST"])
@authentication_classes([TokenAuthentication, ])
@permission_classes([IsAuthenticated])
def add_spending_category(request):
    try:
        user = User.objects.get(username=request.data["user"])
        obj = SpendingCategory(family=user,
                               title=request.data["title"],
                               description=request.data["description"])
        obj.save()
        serializer = SpendingCategorySerializer(obj)
        return Response(serializer.data)
    except ObjectDoesNotExist as error:
        raise Exception(f"Ошибка добавления... {error}")
    except IntegrityError as error:
        raise Exception(f"Ошибка добавления... {error}")


@api_view(["POST"])
@authentication_classes([TokenAuthentication, ])
@permission_classes([IsAuthenticated])
def add_income(request):
    try:
        data = request.data["data"]
        user = User.objects.get(username=request.data["user"])
        category = IncomeCategory.objects.get(id=data["category"])
        date = datetime.datetime.strptime(data["date"], "%a %b %d %Y").date()
        obj = Income(family=user, created_at=date, category=category,
                     description=data["description"], amount=data["amount"])
        obj.save()
        return Response("ok")
    except Exception as error:
        return Response(error)


@api_view(["POST"])
@authentication_classes([TokenAuthentication, ])
@permission_classes([IsAuthenticated])
def add_spending(request):
    try:
        data = request.data["data"]
        user = User.objects.get(username=request.data["user"])
        category = SpendingCategory.objects.get(id=data["category"])
        date = datetime.datetime.strptime(data["date"], "%a %b %d %Y").date()
        obj = Spending(family=user, created_at=date, category=category,
                       description=data["description"], amount=data["amount"])
        obj.save()
        return Response("ok")
    except Exception as error:
        return Response(error)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_plans(request):
    try:
        user = User.objects.get(username=request.data["user"])
        queryset = SpendingPlan.objects.filter(family=user)
        serializer = PlanSerializer(queryset, many=True)
        return Response(serializer.data)
    except Exception as error:
        return Response(error)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_plans(request):
    try:
        for key, value in request.data["data"].items():
            obj = SpendingPlan.objects.get(id=key)
            obj.amount = value
            obj.save()
        return Response("ok")
    except Exception as error:
        return Response(error)
