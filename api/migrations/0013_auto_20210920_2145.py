# Generated by Django 3.0 on 2021-09-20 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_profile_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='liked_profiles',
        ),
        migrations.AddField(
            model_name='likes',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='likes',
            name='bio',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='likes',
            name='breed',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='likes',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
