# Generated by Django 2.2 on 2019-12-11 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0010_courseorg_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseorg',
            name='tag',
        ),
    ]