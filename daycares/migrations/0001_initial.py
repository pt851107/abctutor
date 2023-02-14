# Generated by Django 3.2.16 on 2023-02-14 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Daycare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('discription', models.BooleanField(default=True)),
                ('intro1', models.CharField(max_length=50)),
                ('intro2', models.CharField(max_length=50)),
                ('intro3', models.CharField(max_length=50)),
                ('intro4', models.CharField(max_length=50)),
            ],
        ),
    ]
