# Generated by Django 3.1.1 on 2020-09-17 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_technology'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='percentage',
            field=models.IntegerField(),
        ),
    ]
