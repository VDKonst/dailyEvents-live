# Generated by Django 3.0.2 on 2021-02-12 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210212_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='likes',
            field=models.IntegerField(null=True),
        ),
    ]