# Generated by Django 4.1.1 on 2022-12-20 07:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='hours',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='hours',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hours',
            name='start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]