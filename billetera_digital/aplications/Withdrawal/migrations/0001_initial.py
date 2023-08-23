# Generated by Django 4.2.4 on 2023-08-23 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Withdrawal",
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
            ],
            options={
                "verbose_name": "retiro",
                "verbose_name_plural": "retiro",
                "db_table": "retiro",
            },
        ),
    ]
