# Generated by Django 3.1.3 on 2020-11-25 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20201124_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libadmin',
            name='book_status',
        ),
        migrations.AddField(
            model_name='book',
            name='book_status',
            field=models.BooleanField(default='True', null=True),
        ),
    ]
