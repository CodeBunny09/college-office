# Generated by Django 3.2.9 on 2021-12-23 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20211223_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='PAN_Number',
            field=models.CharField(max_length=10),
        ),
    ]
