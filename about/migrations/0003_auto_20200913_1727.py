# Generated by Django 3.1.1 on 2020-09-13 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_developer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='developer',
            old_name='about_Developer_text',
            new_name='about_developer_text',
        ),
    ]
