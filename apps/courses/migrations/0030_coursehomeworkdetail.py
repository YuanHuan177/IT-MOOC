# Generated by Django 2.2 on 2019-12-08 00:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0029_auto_20191208_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseHomeworkDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('question', models.CharField(max_length=100, verbose_name='题目')),
                ('cone', models.CharField(max_length=100, verbose_name='选项A')),
                ('ctwo', models.CharField(max_length=100, verbose_name='选项B')),
                ('cthree', models.CharField(max_length=100, verbose_name='选项C')),
                ('cfour', models.CharField(max_length=100, verbose_name='选项D')),
                ('answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=2, verbose_name='答案')),
                ('jiexi', models.CharField(max_length=100, verbose_name='解析')),
                ('homework', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='所属作业')),
            ],
            options={
                'verbose_name': '课程作业题目',
                'verbose_name_plural': '课程作业题目',
            },
        ),
    ]