# Generated by Django 5.1.5 on 2025-01-15 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_alter_bestsummithikesactivity_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bestsummithikesactivity",
            name="crowd_level",
            field=models.CharField(
                choices=[
                    ("HE", "Hermit"),
                    ("LO", "Low"),
                    ("MO", "Moderate"),
                    ("HI", "High"),
                ],
                help_text="Enter the lowest crowd level.",
                max_length=2,
            ),
        ),
    ]
