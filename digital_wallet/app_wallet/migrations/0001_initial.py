# Generated by Django 4.2.4 on 2023-09-12 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="withdrawal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code_validation", models.TextField(max_length=200)),
                ("identification_number", models.CharField(max_length=20)),
                (
                    "value",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="cantidad"
                    ),
                ),
            ],
            options={
                "db_table": "withdrawal",
            },
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "transaction_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="fecha_trasaccion"
                    ),
                ),
                (
                    "reference",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="referencia"
                    ),
                ),
                (
                    "reference_name",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="nombre"
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="cantidad"
                    ),
                ),
                ("details", models.TextField(max_length=200)),
                (
                    "transaction_type",
                    models.CharField(max_length=50, verbose_name="category"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_transa",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "Transaction",
            },
        ),
        migrations.CreateModel(
            name="BalanceDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "balance",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="saldo"
                    ),
                ),
                (
                    "deposit_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="fecha_deposito"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_balance",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "BalanceDetail",
            },
        ),
    ]
