# Generated by Django 3.1.3 on 2020-11-30 09:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_auto_20201130_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libadmin',
            name='take_date',
        ),
        migrations.AlterField(
            model_name='libadmin',
            name='give_date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2020, 12, 10, 14, 28, 2, 753914)),
        ),
    ]
