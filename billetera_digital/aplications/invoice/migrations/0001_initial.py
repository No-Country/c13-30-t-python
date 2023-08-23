# Generated by Django 4.2.4 on 2023-08-23 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Invoice",
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
                    "company_name",
                    models.CharField(
                        max_length=50, verbose_name="nombre de la empresa"
                    ),
                ),
                (
                    "reference_number",
                    models.IntegerField(
                        unique=True, verbose_name="numero de referencia"
                    ),
                ),
            ],
            options={
                "verbose_name": "Detalles_identificacion",
                "verbose_name_plural": "factura",
                "db_table": "factura",
                "ordering": ["reference_number"],
            },
        ),
    ]
