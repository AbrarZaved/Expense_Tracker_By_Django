# Generated by Django 5.0.4 on 2024-05-02 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_add_expense_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_expense',
            name='currency',
        ),
    ]
