# Generated by Django 3.2.9 on 2021-12-23 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20211223_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='registration_number_or_usn_number',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
