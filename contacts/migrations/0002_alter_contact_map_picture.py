# Generated by Django 4.1.1 on 2022-09-18 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="map_picture",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="amin-kg/contacts",
                verbose_name="Изображение карты",
            ),
        ),
    ]
