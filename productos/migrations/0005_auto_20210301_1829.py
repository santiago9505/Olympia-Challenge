# Generated by Django 3.1.7 on 2021-03-01 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_auto_20210301_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='stok',
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
    ]
