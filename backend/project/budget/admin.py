from django.contrib import admin

from budget.models import Balance, Spending, Income, SpendingCategory, IncomeCategory, SpendingPlan

admin.site.register(Balance)
admin.site.register(Spending)
admin.site.register(Income)
admin.site.register(IncomeCategory)
admin.site.register(SpendingCategory)
admin.site.register(SpendingPlan)
