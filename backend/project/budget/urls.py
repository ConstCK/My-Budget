from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import register, FamilyViewSet, SpendingViewSet, IncomeViewSet, SpendingCategoryViewSet \
    , IncomeCategoryViewSet, BalanceViewSet, get_main_data

router = routers.DefaultRouter()
router.register('families', FamilyViewSet)
router.register('balance', BalanceViewSet)
router.register('spending', SpendingViewSet)
router.register('income', IncomeViewSet)
router.register('spending-category', SpendingCategoryViewSet)
router.register('income-category', IncomeCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register),
    path('login/', obtain_auth_token),
    path('main-data/', get_main_data),

]
