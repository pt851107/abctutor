# Generated by Django 3.2.16 on 2023-02-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summercamp', '0005_camp_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='activities',
            field=models.TextField(blank=True),
        ),
    ]
