# Generated by Django 5.1.5 on 2025-01-15 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_coloradosnowclimbsactivity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coloradosnowclimbsactivity",
            name="season_text",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
