# Generated by Django 3.2.16 on 2023-02-14 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daycares', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daycare',
            name='discription',
            field=models.CharField(max_length=50),
        ),
    ]