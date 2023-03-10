# Generated by Django 3.2.16 on 2023-02-16 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infantcares', '0002_auto_20230216_0117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infantcare',
            old_name='fees',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='infantcare',
            name='activities',
        ),
        migrations.RemoveField(
            model_name='infantcare',
            name='available',
        ),
        migrations.RemoveField(
            model_name='infantcare',
            name='camp_date',
        ),
        migrations.RemoveField(
            model_name='infantcare',
            name='created',
        ),
        migrations.RemoveField(
            model_name='infantcare',
            name='enrollment_info',
        ),
        migrations.RemoveField(
            model_name='infantcare',
            name='location',
        ),
        migrations.RemoveField(
            model_name='infantcare',
            name='long_description',
        ),
        migrations.RemoveField(
            model_name='infantcare',
            name='payment_details',
        ),
        migrations.RemoveField(
            model_name='infantcare',
            name='photo_1',
        ),
        migrations.RemoveField(
            model_name='infantcare',
            name='photo_2',
        ),
        migrations.RemoveField(
            model_name='infantcare',
            name='photo_main',
        ),
        migrations.RemoveField(
            model_name='infantcare',
            name='safety_info',
        ),
        migrations.RemoveField(
            model_name='infantcare',
            name='short_description',
        ),
        migrations.RemoveField(
            model_name='infantcare',
            name='terms_and_conditions',
        ),
        migrations.RemoveField(
            model_name='infantcare',
            name='updated',
        ),
        migrations.AddField(
            model_name='infantcare',
            name='discription',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='infantcare',
            name='intro1',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='infantcare',
            name='intro2',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='infantcare',
            name='intro3',
            field=models.CharField(default=4, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='infantcare',
            name='intro4',
            field=models.CharField(default=5, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='infantcare',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
