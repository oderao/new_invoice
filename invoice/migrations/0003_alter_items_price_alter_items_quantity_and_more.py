# Generated by Django 4.0.5 on 2022-06-05 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_alter_items_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.PositiveIntegerField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='quantity',
            field=models.PositiveIntegerField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='total',
            field=models.PositiveIntegerField(max_length=200, null=True),
        ),
    ]
