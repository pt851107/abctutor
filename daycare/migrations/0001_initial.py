# Generated by Django 3.2.16 on 2023-02-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('discription', models.TextField(max_length=20)),
                ('intro1', models.CharField(max_length=20)),
                ('intro2', models.CharField(max_length=20)),
                ('intro3', models.CharField(max_length=20)),
                ('intro4', models.CharField(max_length=20)),
            ],
        ),
    ]
