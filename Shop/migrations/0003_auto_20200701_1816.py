# Generated by Django 3.0.5 on 2020-07-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_auto_20200701_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
