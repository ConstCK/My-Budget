from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import FamilyViewSet, SpendingViewSet, IncomeViewSet, SpendingCategoryViewSet \
    , IncomeCategoryViewSet, BalanceViewSet, get_main_data, register, get_income_categories, get_spending_categories, \
    delete_spending_category, delete_income_category, add_income_category, add_spending_category, add_income, \
    add_spending, get_plans, update_plans, get_general_statistic, get_annual_statistic, get_month_statistic

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
    path('get-income-categories/', get_income_categories),
    path('get-spending-categories/', get_spending_categories),
    path('delete-income-category/', delete_income_category),
    path('delete-spending-category/', delete_spending_category),
    path('add-income-category/', add_income_category),
    path('add-spending-category/', add_spending_category),
    path('add-income/', add_income),
    path('add-spending/', add_spending),
    path('get-plans/', get_plans),
    path('update-plans/', update_plans),
    path('statistic/general/', get_general_statistic),
    path('statistic/annual/', get_annual_statistic),
    path('statistic/month/', get_month_statistic),

]
