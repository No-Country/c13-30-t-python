# Generated by Django 4.2.4 on 2023-08-23 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("identification_details", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=50, verbose_name="nombre")),
                (
                    "cell_phone",
                    models.CharField(
                        max_length=10, unique=True, verbose_name="celular"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=100, unique=True, verbose_name="correo"
                    ),
                ),
                (
                    "password",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="contraseña"
                    ),
                ),
                (
                    "create_at",
                    models.DateTimeField(auto_now=True, verbose_name="fecha creaciòn"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(verbose_name="fecha de actualizaciòn"),
                ),
                (
                    "id_identification_details",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="identification_details.identificationdetails",
                    ),
                ),
            ],
            options={
                "verbose_name": "usuario",
                "verbose_name_plural": "usuario",
                "db_table": "usuario",
                "ordering": ["name"],
            },
        ),
    ]
