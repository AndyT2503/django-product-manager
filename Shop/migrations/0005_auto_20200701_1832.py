# Generated by Django 3.0.5 on 2020-07-01 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_auto_20200701_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
