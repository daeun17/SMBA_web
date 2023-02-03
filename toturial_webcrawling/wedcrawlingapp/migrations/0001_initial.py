# Generated by Django 4.1.5 on 2023-02-02 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Melon",
            fields=[
                (
                    "no",
                    models.IntegerField(
                        max_length=13, primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("singer", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "melon",
                "managed": False,
            },
        ),
    ]