# Generated by Django 3.0 on 2021-09-16 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210915_2321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='images',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='profile',
            name='breed',
            field=models.CharField(max_length=100),
        ),
    ]
