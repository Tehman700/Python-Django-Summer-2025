# Generated by Django 5.2.4 on 2025-07-07 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='employee_name',
            new_name='name',
        ),
    ]
