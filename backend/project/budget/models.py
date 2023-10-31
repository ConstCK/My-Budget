from django.contrib.auth.models import User
from django.db import models


class Balance(models.Model):
    family = models.ForeignKey(User, verbose_name="Семья", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата записи")
    balance = models.IntegerField(verbose_name="Текущий баланс")

    def __str__(self):
        return f"Баланс семьи {self.family} на {self.created_at}"

    class Meta:
        verbose_name = "Баланс"
        verbose_name_plural = "Баланс"


class Spending(models.Model):
    family = models.ForeignKey(User, verbose_name="Семья", on_delete=models.CASCADE)
    category = models.ForeignKey("SpendingCategory", verbose_name="Категория расходов"
                                 , related_name="get_spending", on_delete=models.CASCADE, )
    created_at = models.DateField(verbose_name="Дата записи")
    amount = models.PositiveIntegerField(verbose_name="Сумма", default=0)
    description = models.CharField(max_length=512, blank=True, verbose_name="Описание")

    def __str__(self):
        return f"Расход семьи {self.family} на {self.created_at}"

    class Meta:
        verbose_name = "Расход"
        verbose_name_plural = "Расходы"


class Income(models.Model):
    family = models.ForeignKey(User, verbose_name="Семья", on_delete=models.CASCADE)
    category = models.ForeignKey("IncomeCategory", verbose_name="Категория доходов"
                                 , related_name="get_income", on_delete=models.CASCADE,
                                 )
    created_at = models.DateField(verbose_name="Дата записи")
    amount = models.PositiveIntegerField(verbose_name="Сумма", default=0)
    description = models.CharField(max_length=512, blank=True, verbose_name="Описание")

    def __str__(self):
        return f"Доход семьи {self.family} на {self.created_at}"

    class Meta:
        verbose_name = "Доход"
        verbose_name_plural = "Доход"


class SpendingCategory(models.Model):
    family = models.ForeignKey(User, verbose_name="Семья", on_delete=models.CASCADE)
    title = models.CharField(max_length=128, verbose_name="Название расхода")
    description = models.CharField(max_length=512, verbose_name="Описание расхода")

    def __str__(self):
        return f"Расход {self.title} для семьи {self.family}"

    class Meta:
        verbose_name = "Категория расходов"
        verbose_name_plural = "Категории расходов"
        unique_together = ["family", "title"]


class IncomeCategory(models.Model):
    family = models.ForeignKey(User, verbose_name="Семья", on_delete=models.CASCADE)
    title = models.CharField(max_length=128, verbose_name="Название дохода")
    description = models.CharField(max_length=512, blank=True, verbose_name="Описание дохода")

    def __str__(self):
        return f"Доход {self.title} для семьи {self.family}"

    class Meta:
        verbose_name = "Категория доходов"
        verbose_name_plural = "Категории доходов"
        unique_together = ["family", "title"]


class SpendingPlan(models.Model):
    family = models.ForeignKey(User, verbose_name="Семья", on_delete=models.CASCADE)
    category = models.ForeignKey("SpendingCategory", on_delete=models.CASCADE, verbose_name="Категория расходов",
                                 related_name="get_plan")
    amount = models.PositiveIntegerField(verbose_name="Сумма расходов", default=0)
    created_at = models.DateField(auto_now=True, verbose_name="Дата записи")

    def __str__(self):
        return f"План расходов по категории {self.category}"

    class Meta:
        verbose_name = "План расходов"
        verbose_name_plural = "Планы расходов"
