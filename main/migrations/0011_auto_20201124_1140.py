# Generated by Django 3.1.3 on 2020-11-24 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20201124_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='book_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.book'),
        ),
    ]
