# Generated by Django 2.2 on 2019-12-08 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0031_auto_20191208_0014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursehomeworkdetail',
            old_name='homework',
            new_name='name',
        ),
    ]
