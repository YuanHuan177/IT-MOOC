# Generated by Django 2.2 on 2019-12-10 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0039_auto_20191210_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_classics',
            field=models.BooleanField(default=False, verbose_name='是否经典'),
        ),
    ]
