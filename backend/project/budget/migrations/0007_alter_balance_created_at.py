# Generated by Django 4.2.6 on 2023-10-26 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0006_alter_income_amount_alter_spending_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Дата записи'),
        ),
    ]