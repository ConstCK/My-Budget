import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.db.models import Sum, Count, Value, F
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Spending, Income, IncomeCategory, SpendingCategory, Balance, SpendingPlan
from .serializers import UserSerializer, SpendingSerializer, IncomeSerializer, \
    IncomeCategorySerializer, SpendingCategorySerializer, BalanceSerializer, PlanSerializer, GeneralStatisticSerializer


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


@api_view(["GET"])
@authentication_classes([TokenAuthentication, ])
@permission_classes([IsAuthenticated])
def get_main_data(request):
    try:
        current_month = datetime.datetime.now().month
        user = User.objects.get(id=request.user.id)
        balance = Balance.objects.filter(family=user).last().balance
        spending = Spending.objects.filter(family=user, created_at__month=current_month).aggregate(total_spending=Sum(
            "amount", default=0))
        income = Income.objects.filter(family=user, created_at__month=current_month).aggregate(total_income=Sum(
            "amount", default=0))
        return Response({"balance": balance, "spending": spending, "income": income})
    except ObjectDoesNotExist as error:
        raise Exception(f"Отсутствие данных по объекту... {error}")


@api_view(["GET"])
@authentication_classes([TokenAuthentication, ])
@permission_classes([IsAuthenticated])
def get_income_categories(request):
    try:
        user = User.objects.get(id=request.user.id)
        queryset = IncomeCategory.objects.filter(family=user)
        serializer = IncomeCategorySerializer(queryset, many=True)
        return Response(serializer.data)
    except ObjectDoesNotExist as error:
        raise Exception(f"Отсутствие данных... {error}")


@api_view(["GET"])
@authentication_classes([TokenAuthentication, ])
@permission_classes([IsAuthenticated])
def get_spending_categories(request):
    try:
        user = User.objects.get(id=request.user.id)
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
        user = User.objects.get(id=request.user.id)
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
        user = User.objects.get(id=request.user.id)
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
        user = User.objects.get(id=request.user.id)
        category = IncomeCategory.objects.get(id=data["category"])
        date = datetime.datetime.strptime(data["date"], "%a %b %d %Y").date()
        obj = Income(family=user, created_at=date, category=category,
                     description=data["description"], amount=data["amount"])
        obj.save()
        return Response("ok")
    except Exception as error:
        raise Exception(f"Ошибка добавления данных... {error}")


@api_view(["POST"])
@authentication_classes([TokenAuthentication, ])
@permission_classes([IsAuthenticated])
def add_spending(request):
    try:
        data = request.data["data"]
        user = User.objects.get(id=request.user.id)
        category = SpendingCategory.objects.get(id=data["category"])
        date = datetime.datetime.strptime(data["date"], "%a %b %d %Y").date()
        obj = Spending(family=user, created_at=date, category=category,
                       description=data["description"], amount=data["amount"])
        obj.save()
        return Response("ok")
    except Exception as error:
        raise Exception(f"Ошибка добавления данных... {error}")


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_plans(request):
    try:
        user = User.objects.get(id=request.user.id)
        queryset = SpendingPlan.objects.filter(family=user)
        serializer = PlanSerializer(queryset, many=True)
        return Response(serializer.data)
    except Exception as error:
        raise Exception(f"Ошибка получения данных... {error}")


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
        raise Exception(f"Ошибка изменения данных... {error}")


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_general_statistic(request):
    try:
        user = request.user.id
        spending_categories = SpendingCategory.objects.filter(family=user) \
            .annotate(overall=Sum("get_spending__amount", default=0))
        income_categories = IncomeCategory.objects.filter(family=user) \
            .annotate(overall=Sum("get_income__amount", default=0))

        spending_serializer = GeneralStatisticSerializer(spending_categories, many=True)
        income_serializer = GeneralStatisticSerializer(income_categories, many=True)
        return Response({"spending": spending_serializer.data, "income": income_serializer.data})
    except Exception as error:
        raise Exception(f"Ошибка получения данных... {error}")


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_all_statistic(request):
    try:
        user = request.user.id
        spending = Spending.objects.filter(family=user).order_by("created_at")\
            .annotate(category_title=F("category__title"))

        income = Income.objects.filter(family=user).order_by("created_at")\
            .annotate(category_title=F("category__title"))
        spending_serializer = SpendingSerializer(spending, many=True)
        income_serializer = IncomeSerializer(income, many=True)
        return Response({"spending": spending_serializer.data, "income": income_serializer.data})
    except Exception as error:
        raise Exception(f"Ошибка получения данных... {error}")


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_annual_statistic(request):
    try:
        user = request.user.id
        spending_categories = SpendingCategory.objects.filter(family=user,
                                                              get_spending__created_at__year=request.data["year"]) \
            .annotate(overall=Sum("get_spending__amount", default=0))
        income_categories = IncomeCategory.objects.filter(family=user,
                                                          get_income__created_at__year=request.data["year"]) \
            .annotate(overall=Sum("get_income__amount", default=0))
        spending_serializer = GeneralStatisticSerializer(spending_categories, many=True)
        income_serializer = GeneralStatisticSerializer(income_categories, many=True)
        return Response({"spending": spending_serializer.data, "income": income_serializer.data})
    except Exception as error:
        raise Exception(f"Ошибка получения данных... {error}")


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_month_statistic(request):
    try:
        user = request.user.id
        spending_categories = SpendingCategory.objects.filter(family=user,
                                                              get_spending__created_at__year=request.data["year"],
                                                              get_spending__created_at__month=request.data["month"]) \
            .annotate(overall=Sum("get_spending__amount", default=0)).annotate(planned=F("get_plan__amount"))

        income_categories = IncomeCategory.objects.filter(family=user,
                                                          get_income__created_at__year=request.data["year"],
                                                          get_income__created_at__month=request.data["month"]) \
            .annotate(overall=Sum("get_income__amount", default=0))

        spending_serializer = GeneralStatisticSerializer(spending_categories, many=True)
        income_serializer = GeneralStatisticSerializer(income_categories, many=True)
        print(spending_serializer)
        return Response({"spending": spending_serializer.data, "income": income_serializer.data})
    except Exception as error:
        raise Exception(f"Ошибка получения данных... {error}")
