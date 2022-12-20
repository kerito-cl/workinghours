# Generated by Django 4.1.1 on 2022-12-20 07:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_hours_date_alter_hours_end_alter_hours_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hours',
            name='end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='hours',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
