# Generated by Django 4.1.5 on 2023-01-31 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Prod",
            fields=[
                (
                    "prod_id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("prod_name", models.CharField(max_length=40)),
                ("prod_lgu", models.CharField(max_length=4)),
                ("prod_buyer", models.CharField(max_length=6)),
                ("prod_sale", models.IntegerField(max_length=10)),
                ("prod_outline", models.CharField(max_length=50)),
                ("prod_detail", models.TextField(null=True)),
                ("prod_img", models.CharField(max_length=40)),
                ("prod_size", models.CharField(max_length=20, null=True)),
                ("prod_color", models.CharField(max_length=20, null=True)),
                ("prod_delivery", models.CharField(max_length=255, null=True)),
                ("prod_mileage", models.IntegerField(max_length=10, null=True)),
            ],
            options={
                "db_table": "prod",
                "managed": False,
            },
        ),
    ]