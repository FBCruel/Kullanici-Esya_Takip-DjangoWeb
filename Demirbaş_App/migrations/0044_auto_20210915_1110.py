# Generated by Django 3.2.6 on 2021-09-15 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demirbaş_App', '0043_merge_20210915_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='whom',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Etkilenen Kişi'),
        ),
        migrations.AlterField(
            model_name='history',
            name='who',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Kullanıcı Adı'),
        ),
    ]
