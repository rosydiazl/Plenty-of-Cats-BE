# Generated by Django 3.0 on 2021-09-16 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210916_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.CharField(max_length=100),
        ),
    ]
