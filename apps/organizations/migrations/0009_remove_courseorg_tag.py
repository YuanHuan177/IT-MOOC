# Generated by Django 2.2 on 2019-12-11 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0008_courseorg_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseorg',
            name='tag',
        ),
    ]