# Generated by Django 3.2.9 on 2021-12-23 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211223_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='blood_group',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]
