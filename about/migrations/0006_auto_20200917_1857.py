# Generated by Django 3.1.1 on 2020-09-17 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_auto_20200917_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='bar_color',
            field=models.CharField(choices=[('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('info', 'info')], max_length=100),
        ),
    ]
