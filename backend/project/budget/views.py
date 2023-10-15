from django.db import IntegrityError
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Spending, Income, IncomeCategory, SpendingCategory, Balance
from .serializers import UserSerializer, SpendingSerializer, IncomeSerializer, \
    IncomeCategorySerializer, SpendingCategorySerializer, BalanceSerializer


@api_view(['POST'])
def register(request):
    try:
        user = User.objects.create_user(username=request.data['username'],
                                        password=request.data['password'])
        token = Token.objects.create(user=user)
        serializer = UserSerializer(user)
        return Response({'user': serializer.data, 'token': token.key})
    except IntegrityError as error:
        return Response({"error": str(error), "description": "Ошибка регистрации. Возможно пользователь уже "
                                                             "существует"})


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
    return Response("ok")