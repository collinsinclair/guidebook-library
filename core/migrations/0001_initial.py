# Generated by Django 5.1.5 on 2025-01-15 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("first_name", models.CharField(max_length=64)),
                ("last_name", models.CharField(max_length=64)),
                ("website", models.URLField(blank=True, null=True)),
                ("bio", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Publisher",
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
                ("name", models.CharField(max_length=64)),
                ("website", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Guidebook",
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
                ("title", models.CharField(max_length=64)),
                ("subtitle", models.CharField(blank=True, max_length=128, null=True)),
                ("edition", models.IntegerField()),
                ("year_published", models.IntegerField()),
                (
                    "authors",
                    models.ManyToManyField(related_name="guidebooks", to="core.author"),
                ),
                (
                    "publisher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="publications",
                        to="core.publisher",
                    ),
                ),
            ],
        ),
    ]
