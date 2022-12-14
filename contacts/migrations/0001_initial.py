# Generated by Django 4.1.1 on 2022-09-18 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("address", models.CharField(max_length=220, verbose_name="Адрес")),
                (
                    "phone_number",
                    models.CharField(max_length=220, verbose_name="Номер телефона"),
                ),
                ("telegram", models.URLField(verbose_name="Телеграм")),
                ("linedin", models.URLField(verbose_name="Линкедин")),
                ("instagram", models.URLField(verbose_name="Инстаграм")),
                ("youtube", models.URLField(verbose_name="Ютуб")),
                (
                    "map_picture",
                    models.ImageField(
                        upload_to="amin-kg/contacts", verbose_name="Изображение карты"
                    ),
                ),
            ],
            options={
                "verbose_name": "Контакты",
                "verbose_name_plural": "Контакты",
            },
        ),
    ]
