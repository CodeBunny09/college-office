# Generated by Django 3.2.9 on 2021-12-23 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20211223_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='batch',
            field=models.DurationField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='semester',
            field=models.IntegerField(default=0),
        ),
    ]
