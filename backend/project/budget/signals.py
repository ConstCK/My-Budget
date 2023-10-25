from datetime import date, datetime

from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Balance, SpendingCategory, IncomeCategory, Spending, Income


@receiver(post_save, sender=User)
def category_and_balance_creation(sender, instance, created, **kwargs):
    if created:
        Balance.objects.create(family=instance, balance=0, created_at=date.today())

        SpendingCategory.objects.create(family=instance, title="Прочее",
                                        description="Прочие расходы")
        SpendingCategory.objects.create(family=instance, title="Коммуналка",
                                        description="Расходы по оплате жилья и связи")
        SpendingCategory.objects.create(family=instance, title="Еда",
                                        description="Расходы по покупке продуктов питания")
        SpendingCategory.objects.create(family=instance, title="Машина",
                                        description="Расходы по эксплуатации авто")
        SpendingCategory.objects.create(family=instance, title="Транспорт",
                                        description="Расходы на транспорт")
        SpendingCategory.objects.create(family=instance, title="Здоровье",
                                        description="Расходы на лекарства и врачей")
        SpendingCategory.objects.create(family=instance, title="Развлечения",
                                        description="Расходы на кафе, рестораны и другие развлечения")
        SpendingCategory.objects.create(family=instance, title="Одежда",
                                        description="Расходы на покупку одежды")
        SpendingCategory.objects.create(family=instance, title="Питомцы",
                                        description="Расходы на домашних животных")
        SpendingCategory.objects.create(family=instance, title="Обучение",
                                        description="Расходы на обучение")
        SpendingCategory.objects.create(family=instance, title="Дети",
                                        description="Расходы на детей")
        SpendingCategory.objects.create(family=instance, title="Дом",
                                        description="Расходы на содержание жилья и бытовые нужды")
        SpendingCategory.objects.create(family=instance, title="Красота и гигиена",
                                        description="Расходы на себя")
        SpendingCategory.objects.create(family=instance, title="Подарки",
                                        description="Расходы на подарки")
        SpendingCategory.objects.create(family=instance, title="Кредит",
                                        description="Выплата кредита")
        SpendingCategory.objects.create(family=instance, title="Путешествия",
                                        description="Расходы на путешествия")

        IncomeCategory.objects.create(family=instance, title="Прочее",
                                      description="Прочие доходы")
        IncomeCategory.objects.create(family=instance, title="Кредит",
                                      description="Кредитные деньги")
        IncomeCategory.objects.create(family=instance, title="Бизнес",
                                      description="Доходы от бизнеса")
        IncomeCategory.objects.create(family=instance, title="Зарплата",
                                      description="Заработная плата членов семьи")


@receiver(post_save, sender=Spending)
def balance_decreasing(sender, instance, created, **kwargs):
    if created:
        balance = Balance.objects.filter(family=instance.family).last()
        new_balance = int(balance.balance) - int(instance.amount)
        Balance.objects.create(family=instance.family, balance=new_balance,
                               created_at=instance.created_at)


@receiver(post_save, sender=Income)
def balance_increasing(sender, instance, created, **kwargs):
    if created:
        balance = Balance.objects.filter(family=instance.family).last()
        new_balance = int(balance.balance) + int(instance.amount)
        Balance.objects.create(family=instance.family, balance=new_balance,
                               created_at=instance.created_at)
