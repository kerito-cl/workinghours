# Generated by Django 4.1.1 on 2022-12-16 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_days_work_alter_profile_hours_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='author',
        ),
    ]
