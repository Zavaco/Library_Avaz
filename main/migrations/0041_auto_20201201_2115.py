# Generated by Django 3.1.3 on 2020-12-01 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_auto_20201130_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_status',
        ),
        migrations.AddField(
            model_name='libadmin',
            name='book_status',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
