# Generated by Django 3.1.3 on 2020-11-30 08:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_orderlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libadmin',
            name='give_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 10, 13, 10, 59, 179927)),
        ),
    ]
