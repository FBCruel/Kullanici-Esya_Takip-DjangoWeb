# Generated by Django 3.2.6 on 2021-08-17 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Demirbaş_App', '0008_worker_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='person',
            new_name='personD',
        ),
        migrations.RenameField(
            model_name='worker',
            old_name='person',
            new_name='personW',
        ),
    ]
