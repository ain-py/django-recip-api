# Generated by Django 3.2.18 on 2023-03-18 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20230318_0516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_noob',
            new_name='is_Staff',
        ),
    ]