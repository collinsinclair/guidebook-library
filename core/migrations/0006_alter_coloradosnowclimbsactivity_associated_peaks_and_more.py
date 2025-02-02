# Generated by Django 5.1.5 on 2025-01-15 22:48

import django.db.models.deletion
from django.db import migrations, models

import core.models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_alter_coloradosnowclimbsactivity_season_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coloradosnowclimbsactivity",
            name="associated_peaks",
            field=models.ManyToManyField(
                blank=True, related_name="%(class)s_activities", to="core.peak"
            ),
        ),
        migrations.AlterField(
            model_name="coloradosnowclimbsactivity",
            name="guidebook",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(class)s_activities",
                to="core.guidebook",
            ),
        ),
        migrations.AlterField(
            model_name="coloradosnowclimbsactivity",
            name="trailhead",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(class)s_activities",
                to="core.trailhead",
            ),
        ),
        migrations.CreateModel(
            name="BestSummitHikesActivity",
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
                ("guidebook_number", models.IntegerField(blank=True, null=True)),
                (
                    "distance",
                    models.FloatField(help_text="Round-trip distance in miles."),
                ),
                (
                    "gain",
                    models.IntegerField(help_text="Total elevation gain in feet."),
                ),
                (
                    "estimated_time_enroute",
                    models.IntegerField(blank=True, help_text="In minutes.", null=True),
                ),
                (
                    "yds_class",
                    models.FloatField(
                        blank=True,
                        help_text="Enter the highest grade in the case of multiple. Use .5 for +. e.g. 2/3+ -> 3.5.",
                        null=True,
                    ),
                ),
                (
                    "season_bitmap",
                    models.CharField(
                        blank=True,
                        max_length=12,
                        null=True,
                        validators=[core.models.validate_binary_string],
                    ),
                ),
                (
                    "season_text",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                ("difficulty", models.FloatField()),
                (
                    "crowd_level",
                    models.CharField(
                        help_text="Enter the lowest crowd level.", max_length=2
                    ),
                ),
                (
                    "associated_peaks",
                    models.ManyToManyField(
                        blank=True, related_name="%(class)s_activities", to="core.peak"
                    ),
                ),
                (
                    "guidebook",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="%(class)s_activities",
                        to="core.guidebook",
                    ),
                ),
                (
                    "trailhead",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="%(class)s_activities",
                        to="core.trailhead",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
