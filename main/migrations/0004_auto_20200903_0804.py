# Generated by Django 3.0.8 on 2020-09-03 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_data_esp_mem_data_esp_t'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data_esp',
            name='mac_adr',
        ),
        migrations.DeleteModel(
            name='davlenie',
        ),
        migrations.DeleteModel(
            name='temperatura',
        ),
        migrations.DeleteModel(
            name='data_esp',
        ),
    ]
