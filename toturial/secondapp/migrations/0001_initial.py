# Generated by Django 4.1.5 on 2023-01-27 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                ("iprod_id", models.IntegerField(max_length=10)),
                (
                    "iprod_gu",
                    models.CharField(max_length=4, primary_key=True, serialize=False),
                ),
                ("iprod_nm", models.CharField(max_length=40)),
            ],
            options={
                "db_table": "iprod",
                "managed": False,
            },
        ),
    ]
