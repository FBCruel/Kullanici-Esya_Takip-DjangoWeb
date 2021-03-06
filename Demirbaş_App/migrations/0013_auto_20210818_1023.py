# Generated by Django 3.2.6 on 2021-08-18 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demirbaş_App', '0012_alter_device_stok'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='brand',
            field=models.CharField(blank=True, max_length=30, verbose_name='Marka'),
        ),
        migrations.AlterField(
            model_name='device',
            name='device',
            field=models.CharField(blank=True, max_length=20, verbose_name='Cihaz'),
        ),
        migrations.AlterField(
            model_name='device',
            name='exp',
            field=models.CharField(blank=True, max_length=100, verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='device',
            name='number',
            field=models.CharField(blank=True, max_length=5, verbose_name='Sayı'),
        ),
        migrations.AlterField(
            model_name='device',
            name='serial',
            field=models.CharField(blank=True, max_length=50, verbose_name='Seri No'),
        ),
        migrations.AlterField(
            model_name='device',
            name='status',
            field=models.CharField(blank=True, max_length=10, verbose_name='Durumu'),
        ),
    ]
